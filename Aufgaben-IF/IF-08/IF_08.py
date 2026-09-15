'''
If08:
Sepps Tanke befindet sich an der A565 in Bonn am Rande der Eifel. Die nächsten 200 Kilometer gibt es keine weitere Tankstelle. 
Schreiben Sie ein Programm, das den Fahrern hilft zu entscheiden, ob sie tanken sollen oder nicht. 

Das Programm fragt nach:
- Der Tankkapazität in Litern
- Der Benzinanzeige in Prozent (voll = 100, dreiviertel voll = 75, usw.)
- Dem Benzinverbrauch des Fahrzeugs in km pro Liter.

Die Ausgabe des Programms ist „Tanken!“ oder „Weiterfahren“, je nachdem, ob das Fahrzeug genug Benzin für 200 Kilometer hat oder nicht.
'''

tank = int(input("Geben Sie die Tankkapazität in Litern ein: "))
anzeige = int(input("Geben Sie den aktuellen Benzinstand in Prozent ein: "))
verbrauch = float(input("Geben Sie den Verbrauch km/l ein: "))
erg = (tank * anzeige )/100 *verbrauch
if erg < 200:
    print("Tnken!")
else :
    print("Weiterfahren.")
