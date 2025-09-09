#Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen
# ja hemoglobiiniarvon (g/l). Ohjelma ilmoittaa, onko hemoglobiiniarvo
# alhainen, normaali vai korkea.

#Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

sukupuoli = (input("Kerro sukupuolesi (nainen / mies): "))
arvo = int(input("Kerro hemoglobiiniarvo (g/l): "))

if sukupuoli == "nainen":
    if arvo < 117:
        print("Hemoglobiini on alhainen.")
    if arvo >= 117 and arvo <= 175:
        print ("Hemoglobiini on normaali")
    if arvo > 175:
        print ("hemoglobiini on korkea")
else:
    sukupuoli == "mies"
    if arvo < 134:
        print ("Hemoglobiini on alhainen.")
    if arvo >= 134 and arvo <= 195:
        print ("Hemoglobiini on normaali")
    if arvo > 195:
        print ("hemoglobiini on korkea")

