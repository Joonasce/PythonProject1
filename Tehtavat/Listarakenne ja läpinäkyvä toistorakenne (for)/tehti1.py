# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
# Käytä for-toistorakennetta.

import random

lukumaara = int (input("Montako arpakutiota?"))

summa = 0

for i in range (lukumaara):
    noppa = random.randint(1,6)
    summa += noppa

print ("Arpakuutioiden summa on:", summa)
