import datetime
import re

def xor():
    nb = "10001101"
    b8 = nb[7]
    b5 = nb[4]
    b3 = nb[2]
    print(b8)
    print(b5)
    print(b3)
    y = int(b3,2) ^ int(b5,2) ^ int(b8,2)
    print('{0:b}'.format(y))
    nb.del[7]
    nb.add[]
xor()