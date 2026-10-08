'''
Aufgabe for.13
Entwickeln Sie ein Programm mit Schleifen, das ein Sägezahnblatt wie folgt ausgibt:
*
***
*****
*******
*********
***********
*************
'''
for i in range(7):
    for j in range (14):
        if j == 2*i +1 :
            print ('*'*j ,end = '')
    print()

#Herr Adams
for i in range (7):
    for j in range (2*i+1):
        print ('*' ,end = '')
    print()
