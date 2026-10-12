'''Array10
Schreiben Sie ein Programm, das die Elemente in einem Array in aufsteigender Reihenfolge sortiert.
Dabei soll der Nutzer zuerst das Array mit beliebigen Werten füllen können.
Das unsortierte und sortierte Array sollen später ausgegeben werden.
Ohne die Verwendung einer Array-Funktion!
'''
import random


anzahl = int(input("Geben Sie die Anzahl der Elemente im Array ein: "))
arr=[0] * anzahl
from random import randint 
arr=[randint(1, 50) for i in range(anzahl)]
for r in arr:
        print(r, end=" ")
for i in range (anzahl):
    for i in range (1,anzahl):
        if arr[i] > arr[i-1]:
            (arr[i], arr[i-1]) = (arr[i-1], arr[i])
print()
for r in arr:
        print(r, end=" ")
print('_'*45,end ='')
print()
ar1=[] * anzahl
for i in range (anzahl):
    zahl=int(input(f"Geben Sie die Zahl für das {i+1}. Element ein: "))
    ar1.append(zahl) 
for r in ar1:
    print(r,end=' ')
for i in range (anzahl):
    for i in range (1, anzahl):
        if ar1[i] > ar1[i-1]:
            (ar1[i],ar1[i-1]) = (ar1[i-1],ar1[i])
print()
for r in ar1:
    print(r,end=' ')
