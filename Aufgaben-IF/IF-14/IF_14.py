
auswahl=str(input("""Möchten Sie Seitenlängen oder Winkel eingeben?\nFür Seitenlängen drücken Sie bitte 'S/s'.
Für Winkel drücken Sie bitte 'W/w': """))
if auswahl == "s" or auswahl == "S":
    a = float(input("Geben Sie die Länge der ersten Seite ein: "))
    b = float(input("Geben Sie die Länge der zweiten Seite ein: "))
    c = float(input("Geben Sie die Länge der dritten Seite ein: "))
    if a+b>c and a+c>b and b+c>a:
        if a == b == c:
            print("Das Dreieck ist gleichseitig.")
        elif (a == b or a == c or b == c):
            print("Das Dreieck ist gleichschenklig.")
        else:
            print("Das Dreieck ist beliebig.")
    else:
        print("Die eingegebenen Seiten bilden kein Dreieck.")
elif auswahl == "w" or auswahl == "W":
    e = float(input("Geben Sie den Winkel zwischen Seite a und b ein: "))
    f = float(input("Geben Sie den Winkel zwischen Seite a und c ein: "))
    g = float(input("Geben Sie den Winkel zwischen Seite b und c ein: "))
    if e+f+g==180:
        if e<90 and f<90 and g<90:
            print("Das Dreieck ist spitzwinklig.")
        elif (e==90 or f == 90 or g == 90):
            print("Das Dreieck ist rechtwinklig.")
        else:
            print("Das Dreieck ist beliebig.")
    else:
        print("Die eingegebenen Seiten bilden kein Dreieck.")
else:
    print("Sie haben eine ungültige Eingabe eingegeben.")

