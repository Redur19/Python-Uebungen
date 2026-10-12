'''AufgabeTag14_L1_3 
Schreiben Sie ein Programm mit einer Schleife,
die die ersten 100 Quadratzahlen ermittelt und diese Zahlen zusammenzählt.
'''
summe= 0 #ist bis 100 nicht 10
for i in range(1,11):
    for j in range (1,11):
        if i == j:
            summe+= i*j
            print(i * j , end="  ")
print(F"\nDie Summe von diesen Quadrarzahl:{summe} ")

print("\n"+'_'*50)

#Herr Adams
summe = 0
for i in range (1,101):
    q = i**2   #Quadratzahl
    summe += q
    print(F"{i:3d} {q:5d}")
print(F"\nDie Summe von diesen Quadrarzahl:{summe} ")
            
