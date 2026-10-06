''' Aufgabe if.01
Bei einem Wettbewerb müssen alle Teilnehmer in der Schwergewichtsklasse
zwischen 235 (incl)und 265 Pfund wiegen (1 Pfund = 0.5 kg). Schreiben Sie
ein Programm, das nach dem Gewicht des Teilnehmers in Kilogramm fragt und
dann ausgibt, ob er zum Wettbewerb zugelassen ist. '''

print('   Herzlichen Willkommen'+ '\n')

gewicht = float(input('Geben Sie Gewicht in Kilo ein bitte: '))
        
gewicht = gewicht*2 #kilo in Pfund umwandeln.

if (gewicht <= 265 and gewicht >= 235):
    print ('\nSie sind zugelassen')
    
else :
    print("Sie sind leider nicht zugelassen")

print ('\nEnde')
