'''Aufgabe if.06
Schreiben Sie ein Programm zur Berechnung von Schaltjahren. Ob ein Jahr ein
Schaltjahr ist, hängt von mehreren Bedingungen ab:
Ist ein Jahr durch 400 ohne Rest teilbar, ist es immer ein Schaltjahr.
Ist ein Jahr durch 4, jedoch nicht durch 100 teilbar, ist es ein Schaltjahr.
In allen anderen Fällen ist es kein Schaltjahr.
Schreiben Sie ein Programm, das nach einer Jahreszahl fragt und danach
überprüft, ob es sich bei dem Jahr um ein Schaltjahr handelt.
Nach der Prüfung soll ausgegeben werden, ob es ein Schaltjahr ist oder nicht.'''

eingabe =int(input("Für welches Jahr möchten Sie überprüfen,\
 ob es ein Schaltjahr ist: "))
jahr = ' kein '
if eingabe % 400 ==0  or (eingabe % 4 == 0 and eingabe %100 != 0) :
    jahr = ' ein ' #brauchen hier Klammern nicht, da 'and' stärker als 'or' ist.

print(f'Das Jahr {eingabe} ist{jahr}Schaltjahr')
