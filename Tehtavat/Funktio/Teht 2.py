# Muokkaa edellistä funktiota siten, että funktio saa parametrinaan
# nopan tahkojen yhteismäärän. Muokatun funktion avulla voit heitellä
# esimerkiksi 21-tahkoista roolipelinoppaa. Edellisestä tehtävästä poiketen
# nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
# joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random

def heita_noppaa(tahkoja):
    luku = random.randint(1, tahkoja)
    return luku

maksimi = int(input("Anna maksimisilmäluku: "))

silmaluku = 0

while silmaluku != maksimi:
    silmaluku = heita_noppaa(maksimi)
    print (silmaluku)