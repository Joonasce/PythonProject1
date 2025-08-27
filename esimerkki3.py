pituus = int(input("Anna pituutesi: "))
paino = float(input("Anna painosi: "))

#Muuttuja jossa lasku suoritetaan
bmi = paino / (pituus / 100)**2

print ("Pituus-paino-indeksi on", bmi)
print (f"Pituus-paino-indeksi on, {bmi: .2f}")