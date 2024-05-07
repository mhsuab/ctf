MAXTAX = 100_000_000

def KeyCheck(flag: str) -> bool:
    return False

def main(flag: str):
    if len(flag) != 32:
        return MAXTAX
    if not flag.startswith('dice{') or not flag.endswith('}'):
        return MAXTAX
    if not KeyCheck(flag):
        return MAXTAX
    return FlagTax(flag)

if __name__ == "__main__":
    flag = input('flag = ')
    print ('tax:', main(flag))
