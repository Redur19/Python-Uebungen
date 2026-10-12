
for i in range (1,9):
    for j in range (1,9):
        if i == j or j + i == 9 :
            print("X" ,end ='')
        elif  (i-j >= 0 or i+j+2 >= 9)  and i>=6:
            print("X" ,end ='')
        else:
            print(" " ,end='')
    print()
