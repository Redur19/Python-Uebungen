print("Willkommen zu Aladins Schatzsuche")
name= str(input("Geben Sie den Namen der Spielfigur ein: "))
starke= int(input("Stärke eingeben (1-10): "))
gesund = int(input("Gesundheit eingeben (1-10): "))
gluck = int(input("Glück eingeben (1-10): "))
if starke + gesund + gluck > 15:
    starke = gesund = gluck = 5
    print("Sie haben Ihrer Spielfigur zu viele Punkte gegeben!")
print(f"{name}, Stärke: {starke}, Gesundheit: {gesund}, Glück: {gluck}")
