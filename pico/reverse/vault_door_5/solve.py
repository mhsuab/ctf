from base64 import b64decode
encoded_flag = 'JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVmJTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2JTM0JTVmJTM4JTM0JTY2JTY0JTM1JTMwJTM5JTM1'
flag_urlencoded = b64decode(encoded_flag).decode()
flag = [chr(int(c, 16)) for c in flag_urlencoded.split('%')[1:]]

print (f"picoCTF{{{''.join(flag)}}}")