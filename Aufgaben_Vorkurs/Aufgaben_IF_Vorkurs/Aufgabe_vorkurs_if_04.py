'''Aufgabe if.04
Verändern Sie das Programm aus Aufgabe if.03 so, dass ab einem Gewicht
von 20 Kilo 0.50 Euro für jedes Kilo über 10 Kilo zu bezahlen sind.
Gewicht der Sendung: 25   ->   Versandkosten: 10,50 Euro
'''

from math import ceil
gewicht = float(input('Wie viel Kilo wiegt Ihr Paket: '))
grundgebuehr = 3.00

if gewicht <= 10 :
    gebuehr= grundgebuehr
elif 10 < gewicht < 20 :
    gebuehr= grundgebuehr + ceil(gewicht - 10 )*0.25
else :
    gebuehr= grundgebuehr + ceil(gewicht - 10 )*0.5

print(f'Gebühr beträgt: {gebuehr : 5.2f} €. ')
