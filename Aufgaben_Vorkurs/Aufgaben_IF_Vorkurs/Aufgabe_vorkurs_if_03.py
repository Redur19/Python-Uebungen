'''Aufgabe if.03
Ein Paketdienst berechnet 3,00 Euro Versandkosten bis zu einem Gewicht
von 10 Kilo (inklusive). Darüber sind für jedes Kilo zusätzlich 0,25 Euro
zu bezahlen. Schreiben Sie ein Programm, das den Anwender nach dem Gewicht
der Sendung fragt und dann die Versandkosten ausgibt.
Funktion math.ceil() – rundet auf.
Gewicht der Sendung: 11   ->   Versandkosten: 3,25 Euro'''

from math import ceil  
gewicht = float(input('Wie viel Kilo wiegt Ihr Paket: '))
grundgebuehr = 3.00

if gewicht <= 10 :
    gebuehr= grundgebuehr
else :
    gebuehr= grundgebuehr + ceil(gewicht - 10 )*0.25

print(f'Gebühr beträgt: {gebuehr : 5.2f} €. ')

#mein aber falsch.

gewicht = float(input('Wie viel Kilo wiegt Ihr Paket: '))
gebuehr = 3.00
x= gewicht - 10
y= x*0.25 + gebuehr
if gewicht <= 10:
    print(f'Gebühr beträgt: {gebuehr : 5.2f} €. ')
else :
    print(f'Gebühr beträgt: {y : 5.3f} €. ')
#dieses Program ist falsch weil von 10.01 kilogram bis 11 muss das Gebühr
# 3.25 sein und bei diesem Programm ist es nicht so.
