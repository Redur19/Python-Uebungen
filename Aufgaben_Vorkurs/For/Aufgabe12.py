'''Aufgabe for.12
Entwickeln Sie ein Programm mit Schleifen, das diese Figur darstellt.
X------
-X-----
--X----
---XXXX
--X----
-X-----
X------
'''
for i in range(7):
    for j in range (4):
        if i ==j or i>3 and i+j ==6:
            print ('x' , end ='')
        else:
            print ('-' , end ='')
    for a in range (3):
        if i == 3:
            print ('x' , end ='')
        else:
            print ('-' , end ='')
    print()
    
        
#Herr Adams
for i in range(7):
    for j in range (7):
        if (i ==j or i+j == 6 ) and j < 4 or i == 3 and j >= 4:
            #قسم الكود لقسمين عبر كتابة and
            print('X',end='')
        else:
            print('-' ,end ='')
    print()
