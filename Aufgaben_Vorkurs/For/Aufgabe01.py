'''Aufgabe for.01
Schreiben Sie ein Programm, das über eine for-Schleife von 0 bis 3.229 läuft.
Geben Sie bei jedem Schritt den Wert des Schleifenzählers aus.'''

for bum in range(0, 3230):
    print(bum)


#bessere Methode

for i in range(3230):
    print(f'{i:5d}', end="") #end lasst es nicht zu neuer Zeile gehen.
    if i % 10 == 0:
        print() #Zeilenumbruch
