import datetime
from collections import Counter
import re
import csv
import time

def gen1():
    a = 16807 #valeur permettant d'éviter la linéarité
    b = 0 #valeur permettant d'éviter la linéarité
    m = 31
    k = datetime.datetime.now()
    k = str(k)
    ms = re.findall("([0-9]{6})", k)
    ms1 = ms[0]
    ms2 = int(ms1)
    print(ms2)
    print(type(ms2))
    k = ms2
    k=5
    f = ((a*k)+b)%((2**m)-1)
    return f


def alea():
    k = int(gen1())
    liste = [k]
    for i in range(500):
        a = 6
        b = 2
        m = 24
        f = ((a*k)+b)%((2**m)-1)
        k = f
        liste.append(k)
        g = open("liste_gen_periode.txt", "a")
        nb = str(k)+"\n"
        g.write(nb) 
    c = Counter(liste)
    g.write(c)
    print(c)
alea()
