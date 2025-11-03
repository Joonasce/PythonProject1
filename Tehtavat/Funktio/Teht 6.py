#Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä
# sekä pizzan hinnan euroina. Funktio laskee ja palauttaa pizzan yksikköhinnan euroina
# per neliömetri. Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä
# ilmoittaa, kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

import math

def yksikkohinta (halkaisija, hinta):
    sade = halkaisija / 2
    pinta_ala = math.pi * sade ** 2
    pinta_ala_m2 = pinta_ala / 10000
    yksikkohinta = hinta / pinta_ala_m2
    return yksikkohinta

hinta1 = float(input("Anna ensimmäisen pizzan hinta: "))
halkaisija1 = float(input("Anna ensimmisen pizzan halkaisija: "))

hinta2 = float(input("Anna toisen pizzan hinta: "))
halkaisija2 = float(input("Anna toisen pizzan halkaisija: "))

pizza1 = yksikkohinta(halkaisija1, hinta1)
pizza2 = yksikkohinta(halkaisija2, hinta2)

print (f"Ensimmäisen pizzan yksikköhinta on: {pizza1: .2f} €/m2.")
print (f"Toisen pizzan yksikköhinta on: {pizza2: .2f} €/m2.")

if pizza1 < pizza2:
    print ("Ensimmäinen pizza on parempi ostos.")
elif pizza1 > pizza2:
    print ("Toinen pizza on parempi ostos.")
else:
    print ("Molemmat pizzat ovat hyvä ostos. ")






