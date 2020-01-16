#!/usr/bin/python3
from functools import partial
import random
import string

p = partial(print, end='')

index_set = string.digits + string.ascii_lowercase
char_set = string.ascii_letters + string.digits

def page(n):
    header = f'Page {n}'
    print(f'{header:<36}')

    p(f' ' * 2)
    for i in range(16):
        p(f'{index_set[i]:>2}')
    print()

    for i in range(16):
        p(f'{index_set[i]:>2}')
        for k in range(16):
            random.seed()
            c = random.choice(char_set)
            p(f'{c:>2}')
        print()

    print()

def page2(n):
    header = f'Page {n}'
    p(f'{header:<36}')
    header = f'Page {n+1}'
    p(f'{header:<36}')
    print()

    p(f' ' * 2)
    for i in range(16):
        p(f'{index_set[i]:>2}')
    p(f' ' * 2)
    p(f' ' * 2)
    for i in range(16):
        p(f'{index_set[i]:>2}')
    print()

    for i in range(16):
        p(f'{index_set[i]:>2}')
        for k in range(16):
            random.seed()
            c = random.choice(char_set)
            p(f'{c:>2}')

        p(f' ' * 2)

        p(f'{index_set[i]:>2}')
        for k in range(16):
            random.seed()
            c = random.choice(char_set)
            p(f'{c:>2}')

        print()

    print()

for i in range(1, 7, 2):
    page2(i)
