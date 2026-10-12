'''AufgabeTag14_L1_6 '''
for i in range (21,42):
    if i % 5 ==0:
        i -=5
    print(i, end=" ")

print("\n"+'-'*50)

#2 Variante
for i in range (21,42):
    if i % 5 ==0:
        print(i-5, end=" ")
    else:
        print(i, end=" ")
