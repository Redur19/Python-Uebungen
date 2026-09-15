import string
tag =input("Nennen Sie mir bitte den heutigen Tag: ")
monat=input("Nennen Sie mir bitte den Monat: ")
if tag.isdigit() and monat.isdigit():
   monat = int(monat)
   tag =int(tag)
else:
    print("Sie haben eine ungültige Eingabe getätigt.")
if  0<monat<13 and 0<tag<32: # and

    if monat == 4 or monat == 5 or (monat == 6 and tag < 21) or (monat == 3 and tag >= 20):
        print("Es ist Frühling.")
    elif (monat == 6 and tag > 20) or monat == 7 or monat == 8 or (monat == 9 and tag < 23):
        print("Es ist Sommer.")
    elif (monat == 9 and tag >= 23) or monat == 10 or monat == 11 or (monat == 12 and tag < 21):
        print("Es ist Herbst.")
    elif (monat == 12 and tag >= 21) or monat == 1 or monat == 2 or (monat == 3 and tag < 20):
        print("Es ist Winter.")
    else:
        print("Sie haben eine ungültige Eingabe getätigt.")
else:
    print("Sie haben eine ungültige Eingabe getätigt.")
