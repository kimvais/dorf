__author__ = 'kparviainen'

from random import randint

def roll(s):
    n, d = (int(_) for _ in s.split('d'))
    return [randint(1,d) for _ in range(n)]