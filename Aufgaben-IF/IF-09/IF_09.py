artikel= str(input("Geben Sie den Artikelname ein:  "))
preis =float(input("Geben Sie den Preis des Artikels ein: "))
express = int(input("Möchten Sie,dass der Artikel per Express verschickt wird:\n1=ja ,0=nein: "))
betrag = 2
if preis < 10 and express == 1:
    betrag += 5
elif preis >= 10 and express == 1:
    betrag += 6
elif preis >= 10 and express == 0:
    betrag += 1
print("Der Gesamtbetrag beträgt: ", betrag)