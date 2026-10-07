anzahl= int(input("Geben Sie die ANzahl der Schüler ein: "))
arr=[0] * anzahl 
fach=str(input("Geben Sie das Fach ein: "))
summe= 0
for i in range (anzahl):
   arr[i]=float(input(f"Geben Sie die Noten für {i+1}. Schüler/in ein: "))
   summe =arr[i] + summe
durchschnitt = summe / anzahl
print(f"Der Durchschnitt in '{fach}' beträgt: {durchschnitt}")

#2. Variante
anzahl= int(input("Geben Sie die ANzahl der Schüler ein: "))
arr=[]
fach=str(input("Geben Sie das Fach ein: "))
summe= 0
for i in range (anzahl):
    print(f"Geben Sie die Noten für {i+1}. Schüler/in ein: ")
    arr.append(float(input()))
    summe =arr[i] + summe
durchschnitt = summe / anzahl
print(f"Der Durchschnitt in {fach} beträgt: {durchschnitt}")