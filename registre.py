import datetime
import re

def xor():
    nb = "10001101"
    nb_liste = []
    for i in range(len(nb)):
        nb_liste.append(nb[i])
    print(nb_liste)

    b_8 = nb_liste[7]
    b_5 = nb_liste[4]
    b_3 = nb_liste[2]
    y = int(b_3,2) ^ int(b_5,2) ^ int(b_8,2)
    print('{0:b}'.format(y))
    del nb_liste[7]
    nb_liste.insert(0,y)
    print(nb_liste)
    xn = y*2**7 + int(nb_liste[1])*2**6 + int(nb_liste[2])*2**5 + int(nb_liste[3])*2**4 + int(nb_liste[4])*2**3 + int(nb_liste[5])*2**2 + int(nb_liste[6])*2**1 + int(nb_liste[7])
    xn = xn/(2**8)
    print(xn)

xor()