import os
import re


def new_date(path):
    new = []
    with open(path) as f:
        for i, line in enumerate(f.readlines()):
            new.append(re.sub(r'sodipodi:role="line">(\d+.\d+.\d+)', 'sodipodi:role="line">26.07.2022', line))
            if 'Sektor' in line:
                print(line)
    with open(path, 'w') as f:
        f.writelines(new)


for file in os.listdir():
    if 'svg' in file:
        print(file)
        new_date(file)
