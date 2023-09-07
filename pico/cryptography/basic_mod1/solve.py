with open('message.txt', 'r') as f:
    raw = f.read().split()

def decrypt(r: str):
    num = int(r) % 37
    if num <= 25:
        return chr(num + ord('a'))
    elif num <= 35:
        return chr(num - 26 + ord('0'))
    else:
        return '_'

print ('picoCTF{' + ''.join(map(decrypt, raw)) + '}')