#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat
# sen palauttaman summan.

def laske_summa(luvut):
    summa = 0
    for luku in luvut:
        summa += luku
    return summa

lista = list(range(1,11))
print(lista)
print(laske_summa(lista))
