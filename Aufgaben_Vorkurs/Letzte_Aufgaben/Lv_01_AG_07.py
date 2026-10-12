'''
AufgabeTag14_L1_7
Schreiben Sie ein Programm, das die folgende Struktur auf dem Bildschirm ausgibt:
|.|.|.|
|.|.|.|
|.|.|.|
|.|.|.|
|.|.|.|
|.|.|.|
|.|.|.|
'''

for i in range (7):
    for j in range (1,8):
        if  j % 2 == 0:
            print('.',end='')
        else:
           print('|',end='')
    print()
