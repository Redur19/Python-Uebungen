'''
Aufgabe if.07
Der Hersteller eines Mikrowellenherds empfiehlt beim Erhitzen
von zwei Portionen 50% mehr Erhitzungszeit und
beim Erhitzen von drei Portionen, die Erhitzungszeit zu verdoppeln.
Das Erhitzen von mehr als drei Portionen wird nicht empfohlen.
Schreiben Sie ein Programm, das den Anwender
nach der Anzahl der Portionen und
nach der Erhitzungszeit für eine Portion fragt.
Das Programm gibt dann die empfohlene Erhitzungszeit aus.
'''

portionen = int(input("Geben sie die Anzahl der Portionen ein: "))
if 1<= portionen <= 3:
    zeit = float(input("Geben sie die Erhitzungszeit in Sekunden für eine Portion ein: "))
    if portionen == 1:
        erhitzungszeit = zeit
    if portionen == 2:
        erhitzungszeit = zeit*1.5
    if portionen == 3:
        erhitzungszeit = zeit*2
    minuten = erhitzungszeit // 60
    sekunden = erhitzungszeit % 60
    print(F"Die Erhitzungszeit für {portionen} Portionen beträgt {minuten:.0f} Minuten und {sekunden:.0f} Sekunden.") 
else:
    print(F"Das Erhitzen für {portionen} Portionen ist nicht empfohlen!")

#2 Variante
portion = int(input('Geben Sie die Anzahl der Portionen ein: '))
if 1 <= portion <= 3:
    z = float(input('Geben Sie die Erhitzungszeit für eine Portion in Sekunden ein: '))
    por = 'Portion'
    if portion == 1:
        z = z
        por = 'Portionen'
    elif portion == 2:
        z = z * 1.5
    elif portion == 3:
        z = z * 2
        por = 'Portion'
    minuten = z // 60
    sekunden = minuten % 60
    print(F'Die Erhitzungszeit für {portion} {por} beträgt: {minuten: .0f} Minuten {sekunden: .0f} Sekunden.')

else:
    print(f'Das Erhitzen für {portion} Portionen ist nicht empfohlen! ')

#3 Variante
portionen = int(input("Geben sie die Anzahl der Portionen ein: "))
if 1<= portionen <= 3:
    zeit = float(input("Geben sie die Erhitzungszeit in Sekunden für eine Portion ein: "))
    erhitzungszeit = (1 + (portionen - 1)*0.5)*zeit
    minuten = erhitzungszeit // 60
    sekunden = erhitzungszeit % 60
    print(F"Die Erhitzungszeit für {portionen} Portionen beträgt {minuten:.0f} Minuten und {sekunden:.0f} Sekunden.")
else:
    print(F"Das Erhitzen für {portionen} Portionen ist nicht empfohlen!")
#4 Variante mein
portion = int(input('Geben Sie die Anzahl der Portionen ein: '))

if 1 <= portion <= 3:
    zeit = float(input('Geben Sie die Erhitzungszeit für eine \
Portion in Sekundenein: '))
    p = 'Portion'
    if portion == 1:
        zeit = zeit
    elif portion == 2:
        zeit = zeit * 1.5
        p = 'Portionen'
    elif portion == 3:
        zeit = zeit * 2
        p = 'Portionen'

    minuten = zeit // 60
    sekunden = zeit % 60
    print(F'Die Erhitzungszeit für {portion} {p} beträgt: {minuten: .0f} \
Minuten {sekunden: .0f} Sekunden.')

else:
    print(f'Das Erhitzen für {portion} Portionen ist nicht empfohlen! ')

