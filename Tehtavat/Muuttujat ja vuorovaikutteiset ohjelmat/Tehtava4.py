#Kirjoita ohjelma, joka kysyy kolme kokonaislukua. Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.

Kokonaisluku1 = int(input("Anna ensimmäinen kokonaisluku:"))
Kokonaisluku2 = int(input("Anna toinen kokonaisluku:"))
Kokonaisluku3 = int(input("Anna kolmas kokonaisluku:"))

summa = Kokonaisluku1 + Kokonaisluku2 + Kokonaisluku3
tulo = Kokonaisluku1 * Kokonaisluku2 * Kokonaisluku3
keskiarvo = (Kokonaisluku1 + Kokonaisluku2 + Kokonaisluku3) / 3

print (f"Kokonaislukujen summa on:{summa: .2f}")
print (f"Kokonaislukujen tulo on: {tulo: .2f}")
print (f"Kokonaislukujen keskiarvo on: {keskiarvo: .2f}")


