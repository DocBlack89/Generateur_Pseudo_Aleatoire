import datetime
from collections import Counter
import re

def gen1():
    a = 6
    b = 2
    m = 24
    # k = datetime.datetime.now()
    # k = str(k)
    # ms = re.findall("([0-9]{6})", k)
    # ms1 = ms[0]
    # ms2 = int(ms1)
    k = 5
    f = ((a*k)+b)%(2**m)
    return f


def alea():
    k = int(gen1())
    liste = [k]
    for i in range(100):
        a = 6
        b = 2
        m = 24
        f = ((a*k)+b)%(2**m)
        k = f
        liste.append(k)
    c = Counter(liste)
    print(c)
    # Occurence après 23 fois
alea()
