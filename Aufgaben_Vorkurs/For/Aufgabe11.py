'''Aufgabe for.11
Entwickeln Sie ein Programm mit Schleifen, das diese Figur darstellt.
---X---
---X---
---X---
XXXXXXX
---X---
---X---
---X---
'''
for i in range (7):
    for j in range(7):
        if i== 3 or j ==3 :
            print ('X' , end ='')
        else:
            print('-' ,end ='')
    print()
