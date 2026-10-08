'''
Aufgabe for.14
Entwickeln Sie ein Programm mit Schleifen, das ein Sägezahnblatt wie folgt ausgibt:
******** 
******* 
****** 
*****
****
***
**
*

'''
for i in range (8):
    for j in range (8):
        if i+j < 8:
            print('*',end ='')
    print()

#Herr Adams
for i in range (8):
    for j in range (8-i):
        print('*' ,end ='')
    print()
