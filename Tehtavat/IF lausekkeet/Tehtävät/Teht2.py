#Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan
# (LUX, A, B, C) ja tulostaa sen sanallisen kuvauksen alla olevan
# luettelon mukaisesti. Tehtävässä on käytettävä if/elif/else-toistorakennetta.

#LUX on parvekkeellinen hytti yläkannella.
#A on ikkunallinen hytti autokannen yläpuolella.
#B on ikkunaton hytti autokannen yläpuolella.
#C on ikkunaton hytti autokannen alapuolella.
#Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa Virheellinen hyttiluokka.


luokka = (input("Kerro hyttiluokkasi (LUX, A, B, C): "))


if luokka == "A":
    print("Ikkunallinen hytti autokannen yläpuolella")
elif luokka == "B":
    print ("Ikkunaton hytti autokannen yläpuolella.")
elif luokka == "C":
    print("Ikkunaton hytti autokannen alapuolella.")
elif luokka == "LUX":
    print("Parvekkeellinen hytti yläkannella")
else:
    print("Virheellinen hyttiluokka.")
