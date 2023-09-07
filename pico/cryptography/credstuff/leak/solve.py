with open('./passwords.txt', 'r') as f:
    passwords = [r[:-1] for r in f.readlines()]

with open('./usernames.txt', 'r') as f:
    usernames = [r[:-1] for r in f.readlines()]

target_user = 'cultiris'

for username, password in zip(usernames, passwords):
    if username == target_user:
        from codecs import decode
        print (decode(password, 'rot13'))
