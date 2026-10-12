'''AufgabeTag14_L2_8
 | | | | |
-+-+-+-+-+-
 | | | | |
-+-+-+-+-+-
 | | | | |
-+-+-+-+-+-
 | | | | |
-+-+-+-+-+-
 | | | | |
'''

for i in range(1,10):
    for j in range (1,12):
        if i % 2 == 1 and j % 2 == 1:
            print(' ', end='')
        elif i % 2 == 1 and j % 2 == 0:
            print('|', end='')
        elif i % 2 == 0 and j % 2 == 1:
            print('-', end='')
        elif i % 2 == 0 and j % 2 == 0:
            print('+', end='')
    print()

print('\n'+'~'*40 + '\n', end='')
#Herr Adams
for i in range (11):
    for j in range (11):
        if i % 2 == 0:
            print("|" if j % 2 ==1 else " " ,end='')
        else:
            print("-" if j % 2 == 0 else "+" ,end='')
    print()
