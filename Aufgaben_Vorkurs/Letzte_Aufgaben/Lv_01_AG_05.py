'''AufgabeTag14_L1_5 '''

for i in range (1,21):
    if i == 2 or i == 3 or i == 7 or i == 8 or i == 12 or i == 13 or i == 17 or i == 18:
        i+=500
    print(i, end= " ")

print("\n"+'-'*50)

#2 Variante
for i in range (1,21):
    if i in {2,3,7,8,12,13,17,18}:
        i+=500
    print(i, end= " ")
print("\n"+'-'*50)
#3 Variante
for i in range (1,21):
    if i % 5 == 2 or i % 5==3:
        i+=500
    print(i, end= " ")
