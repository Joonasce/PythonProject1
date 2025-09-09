#Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa,
# onko annettu vuosi karkausvuosi. Vuosi on karkausvuosi,
# jos se on jaollinen neljällä. Sadalla jaolliset vuodet
# ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.

vuosi = int(input("Anna vuosiluku: "))

if vuosi % 400 == 0:
    print("Tämä on karkausvuosi.")
else:
    if vuosi % 100 == 0:
        print("Tämä ei ole karkausvuosi.")
    else:
        if vuosi % 4 == 0:
            print("Tämä on karkausvuosi.")
        else:
            print("Tämä ei ole karkausvuosi.")