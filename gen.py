import datetime
from collections import Counter
import re
import csv
import time

def gen1():
    a = 16807
    b = 0
    m = 31
    # k = datetime.datetime.now()
    # k = str(k)
    # ms = re.findall("([0-9]{6})", k)
    # ms1 = ms[0]
    # ms2 = int(ms1)
    k = 5
    f = ((a*k)+b)%((2**m)-1)
    return f


def alea():
    k = int(gen1())
    liste = [k]
    temps = time.time()
    temps1 = time.time()
    while (temps1 < (temps+300)):
        a = 16807
        b = 0
        m = 31
        f = ((a*k)+b)%((2**m)-1)
        k = f
        liste.append(k)
        g = open("liste.txt", "a")
        nb = str(k)+"\n"
        g.write(nb)
        temps1 = time.time()    
    c = Counter(liste)
    g.write(c)
    print(c)
alea()
