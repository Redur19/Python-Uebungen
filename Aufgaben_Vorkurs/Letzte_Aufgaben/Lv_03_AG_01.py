'''
AufgabeTag14_L3_1
Schreiben Sie ein Python-Programm, das die folgende Struktur auf dem Bildschirm ausgibt:

X X X X
 X X X 
X X X X
 X X X 
X X X X
 X X X 
X X X X
'''
for i in range (1,8):
    for j in range (1,8):
        if i%2 == 1 and j % 2 ==1:
            print('X',end='')
        elif i%2 == 1 and j % 2 ==0:
            print(' ',end='')
        elif i%2 == 0 and j % 2 ==0:
            print('X',end='')
        elif i%2 == 0 and j % 2 ==1:
            print(' ',end='')
    print()
