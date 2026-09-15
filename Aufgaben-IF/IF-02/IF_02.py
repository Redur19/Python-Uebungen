'''
If02:
Schreiben Sie ein Programm, das die Längen von drei Seiten eines Dreiecks überprüft und die Art des Dreiecks ausgibt 
(z.B., gleichseitig, gleichschenklig oder beliebig).
Arten des Dreiecks:
Gleichseitig: alle Seiten eines Dreiecks sind gleich lang 
(a=5cm, b=5cm, c=5cm)
Gleichschenklig: zwei Seiten (beide Schenkel) sind gleich lang. Die dritte Seite wird Basis genannt
(a=5cm, b=5cm, c=10cm)
Beliebig: alle Seiten haben eine unterschiedliche Länge 
(a=5cm, b=8cm, c=3cm)
Der Nutzer soll alle drei Seiten eingeben können. Anschließend soll nach der Überprüfung die passende Ausgabe erfolgen.

'''
a = float(input("Geben Sie die Länge der ersten Seite ein: "))
b = float(input("Geben Sie die Länge der zweiten Seite ein: "))
c = float(input("Geben Sie die Länge der dritten Seite ein: ")) 
if a+b>c and a+c>b and b+c>a:
    if a == b == c:
        print("Das Dreieck ist gleichseitig.")
    elif a == b or a == c or b == c:
        print("Das Dreieck ist gleichschenklig.")
    else:
        print("Das Dreieck ist beliebig.")
else:
    print("Die eingegebenen Seiten bilden kein Dreieck.")
