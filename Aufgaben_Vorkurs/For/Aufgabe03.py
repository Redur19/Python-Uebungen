'''Aufgabe for.03
Schreiben Sie ein Programm, das über eine for-Schleife von 444 bis 0 läuft.
Geben Sie bei jedem Schritt den Wert des Schleifenzählers aus.'''

for i in range (444,-1,-1):
    print (f'{i:4d}' , end = "") #end= '' unterdrückt Zeilenumbruch
    if i % 5 == 0  :
        print()   # Zeilenumbruch
    

        
