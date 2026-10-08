'''Aufgabe if.02
Eine Bank verfährt nach der folgenden Regel:
Wenn ein Kunde auf seinem Girokonto ein Guthaben von mehr als 1.000 Euro
oder auf seinem Sparkonto ein Guthaben von mehr als 1.500 Euro hat, wird keine
Scheckgebühr erhoben. Andernfalls wird eine Gebühr von 0,15 Euro erhoben.
Schreiben Sie ein Programm, das nach dem Kontostand der beiden Konten fragt
und dann ausgibt, wie hoch die Gebühr ist.'''

print(' Herzlichen Willkommen ')
giro = float(input('Wie hoch ist der Kontostand Ihres Girokontos: ' ))


if 1000 < giro :
    print('wird keine Scheckgebühr von Ihnen erhoben.')
    

else :
    spar = float(input('Wie hoch ist der Kontostand Ihres Sparkontos: '))
    if 1500 < spar :
        print('wird keine Scheckgebühr von Ihnen erhoben.')
    else :
        print ('wird eine Gebühr von 0,15 Euro erhoben.')

print ('Ende: ')
    

#andere VAriant für Herr Adam.

girokonto = float( input("Geben Sie Ihren Girokonto ein: "))
sparkonto = float( input("Geben Sie Ihren Sparkonto ein: "))

gebuehr = 0.15
if girokonto > 1000 or 1500 < sparkonto :
    gebuehr = 0.0
print ( f"Gebühr beträgt :{gebuehr: 4.2f} €. ")
#الرقم 4 يعني العرض الكلي
#الرقم 2 يعني عدد الأرقام بعد الفاصلة
