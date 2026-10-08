'''Aufgabe for.10
Entwickeln Sie ein Programm mit Schleifen, das diese Figur darstellt.
X-----x
-X---X-
--X-X--
---X---
--X-X--
-X---X-
X-----X
'''
for i in range (7):
    for j in range (7):
        if i + j == 6 or i==j:
            print ('X', end='')
        else:
            print ('-' ,end='')
    print()

#2 Variant
    
for i in range(7):
    line = ""               # نبدأ بسطر فارغ
    for j in range(7):
        if j == i or i+j == 6:
            line += "X"
        else:
            line += "-"
    print(line)
