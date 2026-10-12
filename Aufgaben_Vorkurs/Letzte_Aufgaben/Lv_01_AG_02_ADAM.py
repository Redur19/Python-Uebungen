'''AufgabeTag14_L1_2
Ein Prozess arbeitet im Temperaturbereich 94 °C bis 98 °C.
Ist die Temperatur größer oder kleiner, wird die Meldung ausgegeben
(„Temperatur über 98 °C“ oder („Temperatur unter 94 °C“).
Liegt die Temperatur im vorgegeben Bereich erfolgt die Ausgabe „Temperatur OK“.
Die Temperatur-Werte geben Sie per Tastatur ein. 

'''
def SE_float(text):
    while True:
        try:    #Anfang der Sicherheitszone
            zahl = float(input(text))
            return zahl
        except Exception as e:  #Reaktion auf Fehler
            print('Fehler',e.args[0])

            
#Hautprogramm
while True:
    temp = SE_float('Geben Sie der Temperatur-Wert ein: ')
    if temp > 98:
        print(F"Temperatur {temp:.1f}°C über 98 °C")
    elif temp < 94:
        print("Temperatur {temp:.1f}°C unter 98 °C")
    else:
        print("Temperatur {temp:.1f}°C ist OK")
    jajn = input("Erfolgt weitere Eingabe (j/J): ").upper()
    if jajn != 'J':
        print("\" Aufwiedersehen \"")
        break

