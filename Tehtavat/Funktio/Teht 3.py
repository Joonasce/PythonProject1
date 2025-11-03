# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain
# nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma,
# joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä
# aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää
# negatiivisen gallonamäärän. Yksi gallona on 3,785 litraa.

def nestegallona (gallona):
    litra = gallona * 3.785
    return litra

while True:
    maara = float(input("Anna gallonamäärä: "))


    if maara < 0:
        break
    print(nestegallona(maara))