'''AufgabeTag14_L1_1 
Erweitern Sie die AufgabeT14_L1_1 so, dass die Eingabe per Tastatur in einer
Schleife erfolgt. Bei jeder Eingabe soll gefragt werden,
ob weitere Eingabe erfolgt oder nicht.

'''
#sollte ohne While_Schleife sein aber so ist besser
def check(text):
    while True:
        try:
            zahl = float(input(text))
            return zahl
        except Exeption as e:
            print("Fehler",e.args[0])
            
while True:
    temperatur = check("Geben Sie den Temperatur-Wert bitte ein: ")
    if temperatur > 98:
        print("Temperatur über 98 °C")
    elif temperatur < 94:
        print("Temperatur unter 98 °C")
    else:
        print("Temperatur OK")
