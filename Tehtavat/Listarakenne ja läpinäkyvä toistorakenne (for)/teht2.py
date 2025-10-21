# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. Lopuksi ohjelma
# tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille
# argumentiksi reverse=True.

luvut = []

luku = (input("Anna luku tai lopeta painamalla enter:"))

while luku!="":
    kokonaisluku = int (luku)
    luvut.append (kokonaisluku)
    luku = (input("Anna luku tai lopeta painamalla enter:"))

luvut.sort(reverse=True)
print ("Viisi suurintalukua", luvut)


