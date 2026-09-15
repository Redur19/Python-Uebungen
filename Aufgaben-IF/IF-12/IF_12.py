alt = int(input("Alter: "))
kateg = input("Kategorie:\nNormal/Senior/Kind ")
kateg=kateg.upper()
preis = 12.50
if alt <= 17 and kateg == "KIND":
    preis = 8.50
elif 18 <= alt <= 59 and kateg == "NORMAL":
    preis = 12.50
elif alt >= 60 and kateg == "SENIOR":
    preis = 10.00
else:
    print("Die Kategorie passt nicht zum Alter.")
print("Der Preis beträgt: ", preis ,"Euro")
