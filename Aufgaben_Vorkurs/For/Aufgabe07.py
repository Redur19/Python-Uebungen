'''Aufgabe for.07
Schreiben Sie ein Programm, das Integer-Zahlen addiert,
die vom Benutzer eingegeben werden. Das Programm fragt vorher,
wie viele Zahlen addiert werden sollen.
Danach fordert das Programm den Benutzer auf,
die Zahlen nacheinander einzugeben.
Schließlich gibt es das Ergebnis auf dem Bildschirm aus.
Realisieren Sie das Programm mit einer for-Schleife.
Wie viele Integer sollen addiert werden: 2 
Geben Sie einen Integer ein: 3 
Geben Sie einen Integer ein: -4 
Die Summe ist -1'''

anzahl=int(input('wie viele Zahlen möchten Sie addieren: '))
summe = 0
for n in range (anzahl):
    n = int(input('Geben SIe die Zahlen nacheinander ein: '))
    summe += n
print(F'Die Summe ist : {summe}')

#Herr Adams
summe = 0
anzahl=int(input('wie viele Zahlen möchten Sie addieren: '))
for n in range (1,anzahl+1):
    summe = summe + int(input('Geben SIe die Zahlen nacheinander ein: '))
print(F'Die Summe ist : {summe}')

#chech_Funktion
def se_int(text):
    while True:
        try:
            zahl = int(input(text))
            return zahl
        except:
            print('Geben Sie nur integere Zahlen ein')
liste=[]
anzahl = se_int("Wie viele Integer sollem addiert werden?")
for i in range (anzahl):
    liste.append(se_int("Geben Sie einen Integer ein: "))
print(*liste,sep='+',end='=')
print (sum(liste))

#
print('-'*15)
liste = [x*x for x in range(1,10) ]
print(liste)
