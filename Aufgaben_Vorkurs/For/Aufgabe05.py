'''Aufgabe for.05
Schreiben Sie ein Programm, welches das Produkt der ungeraden Zahlen berechnet
Produkt = 1 * 3 * 5 * ... * n
Die Variable n ist eine beliebige Ganzzahl,
bis zu der die Reihe berechnet werden soll. Sie wird vom Anwender eingegeben.
Das Ergebnis soll am Ende der Berechnung ausgegeben werden.'''

i = int(input("Geben Sie eine Zahl ein: "))

summe = 1
for i in range (i,-1,-1):
    if i % 2 != 0 and i > 0:
        summe = summe * i    
print(f'Die Summe : {summe}')

#Herr Adams
n = int(input("Geben Sie die obere Grenze für multiplizierte Zahlen ein: "))
produkt = 1
for n in range (1,n+1,2):
        produkt = produkt * n     #produkt *= n      
print(f'Das Produkt ist: {produkt}')

