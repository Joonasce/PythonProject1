#Leiviskä = 20naulaa
#Naula = 32 luotia
#luoti = 13,3g

leiviska = int(input("Anna leiviskat: "))
naula = int(input("Anna naulat: "))
luoti = int (input("Anna luodit: "))

yhteensa = leiviska * 20 * 32 + naula * 32 + luoti


grammat = yhteensa * 13.3


kilogrammat = int(grammat // 1000)
gramma1 = grammat % 1000


print(f"Massa nykymittojen mukaan: {kilogrammat: .2f} kilogrammaa ja {gramma1: .2f} grammaa")
