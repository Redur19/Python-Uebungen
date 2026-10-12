'''AufgabeTag14_L2_7
Speichern Sie mit Hilfe des Zufallszahlengenerators die Lottozahlen
vom nächsten Samstag in einer eindimensionalen Liste.
Achtung: Keine Lottozahl darf doppelt vorkommen. Viel Glück!

'''
liste= []
zaehler =0
from random import randint

while zaehler < 6:
    zahl = randint(1,49)
    
    if zahl not in liste:
         liste.append(zahl)
         zaehler +=1
        
print(*liste)
