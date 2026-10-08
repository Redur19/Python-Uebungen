'''Aufgabe for.02
Schreiben Sie ein Programm, das über eine for-Schleife von 0 bis 2.000 in Zweier-Schritten läuft.
Geben Sie bei jedem Schritt den Wert des Schleifenzählers aus.'''

for Ibrahima in range (0,2001,2):
    print (Ibrahima)

#Herr Adams

for a in range (0,2001,2):
    print (f'{a: 4d}' , end=' ')  #end= '' unterdrückt Zeilenumbruch
    if (a+2) % 13 == 0:
        print() # Zeilenumbruch
