'''AufgabeTag14_L1_2
Ein Prozess arbeitet im Temperaturbereich 94 °C bis 98 °C.
Ist die Temperatur größer oder kleiner, wird die Meldung ausgegeben
(„Temperatur über 98 °C“ oder („Temperatur unter 94 °C“).
Liegt die Temperatur im vorgegeben Bereich erfolgt die Ausgabe „Temperatur OK“.
Die Temperatur-Werte geben Sie per Tastatur ein. 

'''
def check_float(text):
    while True:
        try:    #Anfang der Sicherheitszone
            zahl = float(input(text))
            return zahl
        except Exception as e:  #Reaktion auf Fehler
            print('Fehler',e.args[0])
def frage(text):
    while True:
        eingabe =str(input(text)).lower()#wandelt alle Großbuchstaben eines Strings in Kleinbuchstaben um
        if eingabe == "j":
            return True
        elif eingabe == "n":
            return False

            
#Hautprogramm
while True:
    temperatur = check_float('Geben Sie der Temperatur-Wert ein: ')
    if temperatur > 98:
        print("Temperatur über 98 °C")
    elif temperatur < 94:
        print("Temperatur unter 98 °C")
    else:
        print("Temperatur OK")
    if frage("Möchten Sie nochmal contorieren j/J oder n/N: ") == False: #geleich if not frage(" ...")
        print("\" Aufwiedersehen \"")
        break

