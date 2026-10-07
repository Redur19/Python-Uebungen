"""Array03
Schreiben Sie ein Programm, das das größte Element in einem Array findet. 
Das Array und das größte Element sollen später als Ausgabe angezeigt werden.
"""
import random
anzahl = int(input("Geben Sie die Anzahl der Elemente im Array ein: "))
arr01 = [0] * anzahl
for i in range (anzahl):
    arr01[i] = random.randint(1, 10)
for i in range (anzahl):
    for i in range(1, anzahl):
        if arr01[i] > arr01[i-1]:
            (arr01[i-1], arr01[i]) = (arr01[i], arr01[i-1])
for i in arr01:
        print(i, end=" ")
print()
print(arr01[0])
