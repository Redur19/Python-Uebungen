'''Aufgabe for.09
Entwickeln Sie ein Programm mit Schleifen, das diese Figur darstellt.
X------
-X-----
--X----
---X---
----X--
-----X-
------X
'''

for i in range (7):
    for j in range (7):
        if i==j:
            print('X',end ='')
        else:
            print('-' , end='')
    print()
    

#2 Variante
for i in range (7):
    for j in range (7):
       a= '-' *i + 'X' + '-' * (6-i)
    print(a)

#3 Variante

for i in range(7):
    line = ""               # نبدأ بسطر فارغ
    for j in range(7):
        if j == i:
            line += "X"
        else:
            line += "-"
    print(line)
