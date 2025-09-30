#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
#kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
#Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.


luvut = []

luku = (input("Anna ensimmäinen luku tai lopeta painamalla enter: "))

while luku!="":
    numeroksi = float(luku)
    luvut.append(numeroksi)
    luku = input("Anna seuraava luku tai lopeta painamalla enter: ")

if luvut:
    print ("Pienin annettu luku: ", min(luvut))
    print ("Suurin anettu luku: ", max(luvut))
