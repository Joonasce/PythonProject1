#Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
#kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
#nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.


import random

kolminumeroinenkoodi = ""
for _ in range(3): kolminumeroinenkoodi += str(random.randint(0, 9))

nelinumeroinenkoodi= ""
for _ in range (4): nelinumeroinenkoodi += str(random.randint(1, 6))

print("kolminumeroinenkoodi:", kolminumeroinenkoodi)

print ("nelinumeroinenkoodi:", nelinumeroinenkoodi)