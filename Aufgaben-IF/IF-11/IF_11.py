vr = int(input("Geben Sie den Reifendtruck rechter Vorderreifen ein: "))
vl = int(input("Geben Sie den Reifendtruck linker Vorderreifen ein: "))
hr = int(input("Geben Sie den Reifendtruck rechter Hinterreifen ein: "))
hl = int(input("Geben Sie den Reifendtruck linker Hinterreifen ein: "))
if vr == vl and hr == hl:
    print("Der Reifendruck ist OK.")
else:
    print("Der Reifendruck ist nicht in Ordnung.")
