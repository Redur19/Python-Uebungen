'''Aufgabe for.06
Entwickeln Sie ein Programm,
das mit Hilfe einer Zählschleife jeden durch 7 teilbaren Wert
zwischen 1 und 100 anzeigt.'''
for i in range (1,100):
    if i % 7 == 0 :
        print (f'{i:4d}' , end = "")
    
#2 Variante
zaehler = 0
for i in range (0,100,7):
    if i != 0:
        print (f'{i:4d}' , end = "")
        zaehler += 1 #extra geschrieben
        if zaehler % 3 == 0:
            print ()
