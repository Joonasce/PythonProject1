#Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
# (käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
# Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä
# kuin ne syötettiin. käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta
# niiden läpikäymiseen.

nimet = []

for i in range (1,6):
    kaupunki = input ("Anna kaupungin nimi: ")
    nimet.append(kaupunki)

for kaupunki in nimet:
    print (f"{kaupunki}")