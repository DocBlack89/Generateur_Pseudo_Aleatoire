import datetime
import re
import random

def xor():
    k = datetime.datetime.now()
    k = str(k)
    ms = re.findall("([0-9]{6})", k)
    ms1 = ms[0]
    ms2 = int(ms1)
    ms2 = bin(ms2)
    nb_liste = []
    for i in range(8):
        nb_liste.append(ms2[i+2])
    b_8 = nb_liste[7]
    b_5 = nb_liste[4]
    b_3 = nb_liste[2]
    y = int(b_3,2) ^ int(b_5,2) ^ int(b_8,2)
    del nb_liste[7]
    nb_liste.insert(0,y)
    xn = y*2**7 + int(nb_liste[1])*2**6 + int(nb_liste[2])*2**5 + int(nb_liste[3])*2**4 + int(nb_liste[4])*2**3 + int(nb_liste[5])*2**2 + int(nb_liste[6])*2**1 + int(nb_liste[7])
    xn = xn/(2**8)
    return xn


def gess():
    nb1 = xor()
    nb2 = xor()
    nb3 = xor()
    nb1 = b'nb1'