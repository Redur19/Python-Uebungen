'''
AufgabeTag14_L2_4
 Gesucht sind zwei natürliche Zahlen in Bereich 1 bis 100,
 deren Summe ihr Produkt teilt: 
Die Analyse führt zu einer Gleichung A*B modulo (A+B) = 0,
wo A und B natürliche Zahlen (positive int-Zahlen) sind.
Erstellen Sie ein Programm.

'''
for i in range (1,101):
    for j in range(1,101):
        if i*j % (i+j) == 0:
            print (i , j)

#Herr Adams
zaehler = 0
for i in range (1,101):
    for j in range(1,101):
        if i*j % (i+j) == 0 and i>=j: #i>=j damit sich die Zahlen nicht zweimal wiederholt 
            print (F"({i :3d} - {j:<3d})",end = "")
            zaehler +=1
            if zaehler % 5 ==0: #um es geordent zu halten
                print()
print(F"Anzahl der Paare : {zaehler} ")
