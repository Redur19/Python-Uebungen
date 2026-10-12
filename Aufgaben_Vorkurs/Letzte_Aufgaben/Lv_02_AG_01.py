'''AufgabeTag14_L2_1
Berechnen Sie einige Fibonacci-Zahlen.
Diese Zahlenfolge ist wie folgt definiert: 
Formel: an = an-2 + an-1
Die ersten zwei Zahlen werden festgelegt (hier 1, 1) 
Beispiel: 1,1,2,3,5,8,13, 21.     
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
print(a,',',b,end=' , ')
for i in range (n):
    if i == n :
        print(c)
    else:
        print(c,end=' , ')
    a=b
    b=c
    c=a+b

print("\n"*2+'-'*50+"\n"*2)

#2 Variante von Chatgbt
liste =[1,1]
n = int(input('Wie viel Fibonacci-Zahlen berechnet werden sollen: '))
for i in range (2,n+2):
        liste.append(i)
        liste[i] =liste[i-2]+liste[i-1]
print(liste)

print("\n"*2+'-'*50+"\n"*2)

#Herr Adams
#vorletzte -> letzte -> neue
vorletzte = 1
letzte = 1
print(F"{vorletzte} {letzte} ",end="")
for i in range(20):
    neue = vorletzte + letzte
    print(F"{neue}",end=" ")
    vorletzte = letzte
    letzte = neue

