#Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
#Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
#Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus,
#Liian pieni arvaus tai Oikein. Huomaa, että tietokone ei saa vaihtaa lukuaan
#arvauskertojen välissä.


import random

kokonaisluku = random.randint(1,10)

while True:
    luku = int (input("Anna seuraava luku: "))

    if luku < kokonaisluku:
        print ("Liian pieni arvaus")
    elif luku > kokonaisluku:
        print ("Liian suuri arvaus")
    else:
        print ("Arvaus oli oikein")
        break



