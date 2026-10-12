'''
AufgabeTag14_L3_4
'''
for i in range (1,5):
    for j in range (1,9):
        if (i == j or j ==9 - i):
            print("X" ,end ='')
        else:
            print(" " ,end='')
    print()
for i in range (1,4):
    print(F' '* (8-i-5) ,end ='')
    print('X'* (i*2+2) ,end ='')
    print()

