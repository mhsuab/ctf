from subprocess import check_output
from tqdm import tqdm

s = 'ver6'
for i in tqdm(range(1000)):
    ret = check_output(f'cd output/{i}; ./beatme < {s}; cd ../..', shell=True)
    if ret == b':)\n':
        pass
    else:
        print (f'wrong: {i}')
