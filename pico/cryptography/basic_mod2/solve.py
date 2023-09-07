with open('message.txt', 'r') as f:
    raw = f.read().split()

def decrypt(r: str):
    num = pow(int(r), -1, 41)
    if num <= 26:
        return chr(num - 1 + ord('a'))
    elif num <= 36:
        return chr(num - 27 + ord('0'))
    else:
        return '_'


print ('picoCTF{' + ''.join(map(decrypt, raw)) + '}')