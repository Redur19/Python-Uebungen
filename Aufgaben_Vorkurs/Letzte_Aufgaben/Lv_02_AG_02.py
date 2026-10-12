'''AufgabeTag14_L2_2
Erweitern Sie die AufgabeT14_L2_1 so, dass zusätzlich  an / an-1  und
an / an-2  bei jedem Durchlauf  berechnet und ausgegeben werden.
Was stellen Sie fest? 
Implizite Konvertierung in Python:

'''
def SE_int(text):
    while True:
        try:
            zahl = int(input(text))
            return zahl
        except Exception as e:
            print("Fehler",e.args[0])

a= SE_int('Geben Sie die erste zahl ein: ')
b= SE_int('Geben Sie die zweite zahl ein: ')
c= a + b
n= SE_int('Wie viele Fibonacci-Zahlen bechnet werden sollen: ')
print(a,b)
for i in range (n):
    print(f"{c} {c/b:.2f} {c/a:.2f}")
    a=b
    b=c
    c=a+b

print("\n"*2+'-'*50+"\n"*2)

#Herr Adams
def SE_int(text):
    while True:
        try:                        #Anfang der Sicherheitszone
            zahl = int(input(text))
            return zahl
        except Exception as e:      #Reaktion auf Fehler
            print(e.args[0])
            
#vorletzte -> letzte -> neue
vorletzte = SE_int("Geben Sie die erste Fibo-Zahl ein: ")
letzte = SE_int("Geben Sie die zweite Fibo-Zahl ein: ")
print(F"{vorletzte} {letzte} ")
for i in range(40):
    neue = vorletzte + letzte
    print(F"{neue:10d} {neue/letzte:17.15f} {neue/vorletzte:17.15f}")
    (letzte,vorletzte)=(neue,letzte)


