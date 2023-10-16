from pwn import *
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from tqdm import tqdm
from typing import Iterator, Callable

'''
Overwrite iter.mbruteforce, which is BUGGY
~> alphabet:str to (alphabet:bytes or alphabet:
'''
import multiprocessing
from itertools import *
def consume(n: int, iterator: Iterator):
    """consume(n, iterator)

    Advance the iterator `n` steps ahead. If `n is :const:`None`, consume
    everything.

    Arguments:
      n(int):  Number of elements to consume.
      iterator(iterator):  An iterator.

    Returns:
      :const:`None`.

    Examples:
      >>> i = count()
      >>> consume(5, i)
      >>> next(i)
      5
      >>> i = iter([1, 2, 3, 4, 5])
      >>> consume(2, i)
      >>> list(i)
      [3, 4, 5]
      >>> def g():
      ...     for i in range(2):
      ...         yield i
      ...         print(i)
      >>> consume(None, g())
      0
      1
    """
    # Use functions that consume iterators at C speed.
    if n is None:
        # feed the entire iterator into a zero-length deque
        collections.deque(iterator, maxlen = 0)
    else:
        # advance to the empty slice starting at position n
        next(islice(iterator, n, n), None)

def bruteforce(func: Callable, alphabet: Iterator, length: int, method: str = 'upto', start = None, databag = None):
    if   method == 'upto' and length > 1:
        iterator = product(alphabet, repeat = 1)
        for i in range(2, length + 1):
            iterator = chain(iterator, product(alphabet, repeat = i))

    elif method == 'downfrom' and length > 1:
        iterator = product(alphabet, repeat = length)
        for i in range(length - 1, 1, -1):
            iterator = chain(iterator, product(alphabet, repeat = i))

    elif method == 'fixed':
        iterator = product(alphabet, repeat = length)

    else:
        raise TypeError('bruteforce(): unknown method')

    if method == 'fixed':
        total_iterations = len(alphabet) ** length
    else:
        total_iterations = (len(alphabet) ** (length + 1) // (len(alphabet) - 1)) - 1

    if start is not None:
        i, N = start
        if i > N:
            raise ValueError('bruteforce(): invalid starting point')

        i -= 1
        chunk_size = total_iterations // N
        rest = total_iterations % N
        starting_point = 0

        for chunk in range(N):
            if chunk >= i:
                break
            if chunk <= rest:
                starting_point += chunk_size + 1
            else:
                starting_point += chunk_size

        if rest >= i:
            chunk_size += 1

        total_iterations = chunk_size

    h = log.waitfor('Bruteforcing')
    cur_iteration = 0
    if start is not None:
        consume(i, iterator)
    for e in iterator:
        # cur = ''.join(e)
        cur = bytes(e)
        cur_iteration += 1
        if cur_iteration % 2000 == 0:
            progress = 100.0 * cur_iteration / total_iterations
            h.status('Trying "%s", %0.3f%%' % (cur, progress))
            if databag:
                databag["current_item"] = cur
                databag["items_done"] = cur_iteration
                databag["items_total"] = total_iterations
        res = func(cur)
        if res:
            h.success('Found key: "%s"' % cur)
            return cur
        if start is not None:
            consume(N - 1, iterator)

    h.failure('No matches found')

def _mbruteforcewrap(func, alphabet, length, method, start, databag):
    oldloglevel = context.log_level
    context.log_level = 'critical'
    res = bruteforce(func, alphabet, length, method=method, start=start, databag=databag)
    context.log_level = oldloglevel
    databag["result"] = res


def mbruteforce(func, alphabet, length, method = 'upto', start = None, threads = None):
    """mbruteforce(func, alphabet, length, method = 'upto', start = None, threads = None)

    Same functionality as bruteforce(), but multithreaded.

    Arguments:
      func, alphabet, length, method, start: same as for bruteforce()
      threads: Amount of threads to spawn, default is the amount of cores.

    Example:
      >>> mbruteforce(lambda x: x == 'hello', string.ascii_lowercase, length = 10)
      'hello'
      >>> mbruteforce(lambda x: x == 'hello', 'hlo', 5, 'downfrom') is None
      True
      >>> mbruteforce(lambda x: x == 'no', string.ascii_lowercase, length=2, method='fixed')
      'no'
      >>> mbruteforce(lambda x: x == '9999', string.digits, length=4, threads=1, start=(2, 2))
      '9999'
    """

    if start is None:
        start = (1, 1)

    if threads is None:
        try:
            threads = multiprocessing.cpu_count()
        except NotImplementedError:
            threads = 1

    h = log.waitfor('MBruteforcing')
    processes = [None] * threads
    shareddata = [None] * threads

    (i2, N2) = start
    totalchunks = threads * N2

    for i in range(threads):
        shareddata[i] = multiprocessing.Manager().dict()
        shareddata[i]['result'] = None
        shareddata[i]['current_item'] = ""
        shareddata[i]['items_done'] = 0
        shareddata[i]['items_total'] = 0

        chunkid = (i2-1) + (i * N2) + 1

        processes[i] = multiprocessing.Process(target=_mbruteforcewrap,
                args=(func, alphabet, length, method, (chunkid, totalchunks),
                        shareddata[i]))
        processes[i].start()

    done = False

    while not done:
        # log status
        current_item_list = ",".join(["\"%s\"" % x["current_item"]
                                for x in shareddata if x is not None])
        items_done = sum([x["items_done"] for x in shareddata if x is not None])
        items_total = sum([x["items_total"] for x in shareddata if x is not None])

        progress = 100.0 * items_done / items_total if items_total != 0 else 0.0

        h.status('Trying %s -- %0.3f%%' % (current_item_list, progress))

        # handle finished threads
        for i in range(threads):
            if processes[i] and processes[i].exitcode is not None:
                # thread has terminated
                res = shareddata[i]["result"]
                processes[i].join()
                processes[i] = None

                # if successful, kill all other threads and return success
                if res is not None:
                    for i in range(threads):
                        if processes[i] is not None:
                            processes[i].terminate()
                            processes[i].join()
                            processes[i] = None
                    h.success('Found key: "%s"' % res)
                    return res

                if all([x is None for x in processes]):
                    done = True
        time.sleep(0.3)
    h.failure('No matches found')

def bxor(a, b):
    return bytes([i ^ j for i, j in zip(a, b)])


def expand_key(key, n):
    if len(key) >= n:
        return key[:n]

    out = key + b"\x00" * (n - len(key))
    for i in range(1, n - len(key) + 1):
        out = bxor(out, b"\x00" * i + key + b"\x00" * (n - len(key) - i))
    return out

def des(key, hash):
    if isinstance(key, str):
        key = key.encode()
    return DES.new(
        expand_key(key, 8), DES.MODE_ECB
    ).encrypt(pad(hash, 16))

# s = remote('handshake.ctf.maplebacon.org', 1337)
s = process('./server.py')
s.recvline()
info = s.recvline()

_, _, (_, (c_resp, c_hash, user)), _ = safeeval.expr(info)

p_hash = mbruteforce(lambda x: des(x, c_hash) == c_resp[:16], range(256), 3, 'fixed')
p_hash += mbruteforce(lambda x: des(x, c_hash) == c_resp[16:32], range(256), 3, 'fixed')
p_hash += mbruteforce(lambda x: des(x, c_hash) == c_resp[32:], range(256), 3, 'fixed')

r_chal = b'noo'
r_resp = des(p_hash[:3], r_chal) + des(p_hash[3:6], r_chal) + des(p_hash[6:], r_chal)
s.recvuntil(b'response: ')
s.sendline(f'{r_resp.hex()} {r_chal.hex()} {user}'.encode())
s.recvline()
print (s.recvline())

