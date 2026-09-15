
a = float(input("Geben Sie die Länge der ersten Seite ein: "))
b = float(input("Geben Sie die Länge der zweiten Seite ein: "))
c = float(input("Geben Sie die Länge der dritten Seite ein: ")) 
e = float(input("Geben Sie den Winkel zwischen Seite a und b ein: "))
f = float(input("Geben Sie den Winkel zwischen Seite a und c ein: "))
g = float(input("Geben Sie den Winkel zwischen Seite b und c ein: "))
if a+b>c and a+c>b and b+c>a and e+f+g==180:
    if a == b == c:
        print("Das Dreieck ist gleichseitig und spitzwinklig.")
    elif (a == b or a == c or b == c):
        if (e==f or f==g or e==g):
            if e>90 or f>90 or g>90:
                print("Das Dreieck ist gleichschenklig und stumpfwinklig.")
            elif e== 90 or f==90 or g==90:
                print("Das Dreieck ist gleichschenklig und rechtwinklig.")
            else:
                print("Das Dreieck ist gleichschenklig und spitzwinklig.")
        else:
            print("Die eingegebenen Seiten und Winklen bilden kein Dreieck.")

    elif a != b or a != c or b != c:
        if e>90 or f>90 or g>90:
            print("Das Dreieck ist beliebig und stumpfwinklig.")
        elif e== 90 or f==90 or g==90:
            print("Das Dreieck ist beliebig und rechtwinklig.")
        elif a<90 and f<90 and g<90:
            print("Das Dreieck ist beliebig und spitzwinklig.")
        else:
            print("Die eingegebenen Seiten bilden kein Dreieck.")
        
else:
    print("Die eingegebenen Seiten und Winkeln bilden kein Dreieck.")

