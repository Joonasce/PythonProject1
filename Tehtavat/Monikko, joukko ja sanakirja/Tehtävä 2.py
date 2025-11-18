#Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka,
# kunnes käyttäjä syöttää tyhjän merkkijonon. Kunkin nimen syöttämisen
# jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen
# mukaan, syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt
# nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä. Käytä
# joukkotietorakennetta nimien tallentamiseen.

nimet = []

while True:
    nimi = (input("Anna nimi:"))
    if nimi == "":
        break
    if nimi not in nimet:
        print ("Uusi nimi")
        nimet.append(nimi)
    else:
        print ("Aiemmin annettu nimi")

print ("Annetut nimet")
for n in nimet:
    print(n)
