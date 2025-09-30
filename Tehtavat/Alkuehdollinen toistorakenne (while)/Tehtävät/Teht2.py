#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes
#käyttäjä antaa negatiivisen tuumamäärän. Sen jälkeen ohjelma lopettaa
#toimintansa. 1 tuuma = 2,54 cm


luku = float (input("Anna tuumamäärä: "))

while luku >= 0:
    sentti = luku*2.54
    print ("Senttimetriä: ", sentti)

    if luku < 0:
        break
