#Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron,
# jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan
# (kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia
# vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten,
# että joulukuu on ensimmäinen talvikuukausi.


vuodenajat = ("Talvi", "Kevät", "Kesä", "Syksy")

kuukaudennumero = int (input("Anna kuukauden numero (1-12): "))

siirto = kuukaudennumero + 1

kuukaudennumero = siirto % 12

ryhmä = kuukaudennumero // 3

vuodenaika = vuodenajat[ryhmä]

print (f"{vuodenaika}")
