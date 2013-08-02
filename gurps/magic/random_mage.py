from spells import MAGERYLEVELS, colours
from random import sample

LEVEL = 4
col =  sample(colours, 1)[0]
print col, tuple(zip(
        sample(colours[col], len(MAGERYLEVELS[LEVEL])),
        MAGERYLEVELS[LEVEL]))

