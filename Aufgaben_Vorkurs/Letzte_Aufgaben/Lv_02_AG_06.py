'''AufgabeTag14_L2_6'''

for i in range (1,11):
    print(i, end = ' ')
print()
for i in range (1,11):
    print(i*2, end = ' ')
print()
for i in range (1,11):
    print(i*3, end = ' ')
print()
for i in range (1,11):
    print(i*5, end = ' ')
print()
for i in range (1,11):
    print(i*6, end = ' ')
print()
for i in range (1,11):
    print(i*7, end = ' ')
print()
for i in range (1,11):
    print(i*8, end = ' ')
print()
for i in range (1,11):
    print(i*9, end = ' ')
print()
for i in range (1,11):
    print(i*10, end = ' ')
print()

print('-'* 50 ,end='\n')
#2 Variante
z=1
n =1
for i in range (1,11):
    for j in range (1,11):
        print(j*z, end = ' ')
    z +=1
    print()
