#Array-01
'''Erstellen sie ein Programm, das folgende Zahlen auf dem Bildschirmausgibt:
1	2	4	7	11	16	22	29	37'''
summe=0
zaehler = 0
for i in range (1,38):
    if i ==2:
        summe=0
        zaehler=0
    summe = summe + i -zaehler
    zaehler +=1
    if zaehler==2:
        zaehler -=1
    if summe > 37:
        break
    print(summe,end=' ')

print()
#Bessere Variante
zahl =1 
for i in range(1,10):
    print(zahl, end='  ')
    zahl = zahl+i