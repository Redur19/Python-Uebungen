'''Aufgabe for.04
Schreiben Sie ein Programm, das die folgende Summe berechnet:
Summe = 1 + 2 + 3 + 4 + ... + n
Die Variable n ist vom Typ int, bis zu dem die Reihe berechnet werden soll.
Sie wird Anwender eingegeben. Das Ergebnis soll am Ende der Berechnung
ausgegeben werden.'''

i = int(input("Geben Sie eine AnZahl der Addierten zahlen ein: "))

sume = 0
for i in range (i,0,-1):
    sume = sume + i   #sume += i  
print(f'Die Summe : {sume}')

#Herr Adams
n = int(input("Geben Sie eine AnZahl der Addierten zahlen ein: "))
summe = 0
for n in range (1,n+1):
    summe += n              #summe = summe + n
print(f'Die Summe von 1 bis {n} : {summe}')
