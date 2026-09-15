
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
    print("Die eingegebenen Seiten und Winkeln bilden kein Dreieck.")