'''If01:
Schreiben sie ein Programm, welches folgende Aufgabe löst:

Ein Paketdienst berechnet 3,00 Euro Versandkosten bis zu einem Gewicht von 10 Kilo
(inklusive). Darüber sind für jedes Kilo zusätzlich 0,25 Euro zu bezahlen. Schreiben Sie
ein Programm, das den Anwender nach dem Gewicht der Sendung fragt und dann die
Versandkosten ausgibt.

Beispiel:
Gewicht der Sendung: 11
Versandkosten: 3,25 Euro
'''
import math
summe = 3.00
eingabe = float(input("Wie viel Kilo wiegt Ihr Paket: "))
eingabe = math.ceil(eingabe)
if eingabe > 10 :
    summe = 3 + (eingabe - 10) * 0.25
    print(f"Versandkosten: {summe} Euro")
else:
    print(summe)
