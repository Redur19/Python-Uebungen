'''Aufgabe if.05
Schreiben Sie ein Programm, mit dem Sie Werte von Euro nach DM und
umgekehrt ausrechnen können. Der Anwender soll dabei nach dem Betrag
gefragt werden und in welche Währung der Betrag umgerechnet werden soll.
Dabei soll das Zeichen 'e' für die Berechnung DM -> Euro ausgewertet werden.
Ist das eingegebene Zeichen ein anderes, soll die Berechnung Euro -> DM erfolgen.
Die Formel die Sie dazu benötigen sind:
Euro = DM/1,95583 bzw.  DM = Euro * 1,95583 '''


#hier wandelt das Programm die Währung in eine Richtung um, wenn wir 'e' drücken.
#in der entgegenfesetzte Richnung in allen anderen Fällen.

wechsel = input("Für DM -> Euro geben Sie \'e\' ein.\
                \nFür Euro -> DM geben Sie \' d \' ein.\
                \n\'e\' oder \'d\': ")
if  wechsel == 'e':
    wert = float(input('Geben Sie den Beitrag in DM ein: ')) /1.95583
    waehrung = ' in Euro '
        

else :
        wert = float(input('Geben Sie den Beitrag in Euro ein: ')) *1.95583
        waehrung = ' in DM'

print(F'Der Beitrag {waehrung}: {wert: .3f} . ')


#Mein Programm wandeltdie Währung nur bei 'e' und 'd' um.

print("Wählen Sie  \' e \' wenn Sie Euro erhalten wollen")
print("Wählen Sie  \' d \' wenn Sie Euro erhalten wollen: ")
while True:
    wechsel = input()
    if  wechsel == 'e':
        wert = float(input('Geben Sie den Beitrag in DM ein: ')) /1.95583
        waehrung = 'Euro '
        break

    elif wechsel == 'd' :
        wert = float(input('Geben Sie den Beitrag in Euro ein: ')) *1.95583
        waehrung = 'DM'
        break
    else :
        print ("Geben Sie bitte entweder \' e \' oder \' d \' ein ")

print(F'Der Beitrag: {wert:.3f} {waehrung}. ')

#Herr Adams Programm

FAKTOR = 1.95583
wechsel = input("Für DM -> Euro geben Sie \'e\' ein.\
                \nFür Euro -> DM geben Sie ein anderes Zeichen ein.\
                \n Ihr Wahl: ")
eingabe = float(input('Geben Sie den Beitrag ein: '))
if  wechsel == 'e':
    print(F'Der Beitrag: {eingabe/FAKTOR: .3f} Euro. ')  

else :
    print(F'Der Beitrag: {eingabe*FAKTOR: .3f} DM. ')





