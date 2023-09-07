'''
linear homogeneous recurrence equation
https://www.wolframalpha.com/input?i=f%28i%29+%3D+55692*f%28i-4%29+-+9549*f%28i-3%29+%2B+301*f%28i-2%29+%2B+21*f%28i-1%29%2C+f%280%29+%3D+1%2C+f%281%29+%3D+2%2C+f%282%29+%3D+3%2C+f%283%29+%3D+4
'''
import hashlib
import sys
import gmpy2

ITERS = int(2e7)
VERIF_KEY = "96cc5f3b460732b442814fd33cf8537c"
ENCRYPTED_FLAG = bytes.fromhex("42cbbce1487b443de1acf4834baed794f4bbd0dfb5885e6c7ed9a3c62b")

def m_func(i):
    i = gmpy2.mpz(i)

    return (
        1612 * pow(-21, i)
        + 30685 * pow(2, 2 * i + 5) * pow(3, i)
        - 1082829 * pow(13, i)
        + 8349 * pow(17, i + 1)
    ) // 42636

# Decrypt the flag
def decrypt_flag(sol):
    sol = sol % (10**10000)
    sol = str(sol)
    sol_md5 = hashlib.md5(sol.encode()).hexdigest()

    if sol_md5 != VERIF_KEY:
        print("Incorrect solution")
        sys.exit(1)

    key = hashlib.sha256(sol.encode()).digest()
    flag = bytearray([char ^ key[i] for i, char in enumerate(ENCRYPTED_FLAG)]).decode()

    print(flag)

if __name__ == "__main__":
    sol = m_func(ITERS)
    decrypt_flag(sol)
