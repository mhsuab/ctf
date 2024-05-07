# cmd = lambda i: f"gdb --batch -ex 'py arg0 = {i}' -x sol.py 2> /dev/null 1> /dev/null"
cmd = lambda i: f'bash -c "pyda sol_pyda.py -- output/{i}/beatme < <(echo aaaaaaaa)"'
# cmd = lambda i: f'docker run --rm -it -v ~/ctfs/mhsuab/defcon32/nloads/output/{i}:/mhsuab -v ~/ctfs/mhsuab/defcon32/nloads/sol_pyda.py:/mhsuab/s.py pyda --extrypoint "pyda /mhsuab/s.py -- /mhsuab/beatme < <(echo aaaaaaaa)"'
# cmd = lambda i: f"docker run --rm -it -v ~/ctfs/mhsuab/defcon32/nloads/output/{i}:/mhsuab -v ~/ctfs/mhsuab/defcon32/nloads/sol_pyda.py:/mhsuab/s.py pyda bash -c 'pyda /mhsuab/s.py -- /mhsuab/beatme < <(echo aaaaaaaa)'"

from subprocess import TimeoutExpired, run, DEVNULL
from tqdm import tqdm
from multiprocessing import Pool

def f(i):
    try:
        run(cmd(i), shell=True, stdout=DEVNULL, timeout=.4)
    except TimeoutExpired:
        pass

if __name__ == '__main__':
    count = 2000
    with Pool(15) as p:
        list(tqdm(p.imap(f, range(3000, 3000 + count)), total=count))

