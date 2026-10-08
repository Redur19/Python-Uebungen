'''
Aufgabe for.15
Entwickeln Sie ein Programm mit Schleifen, das einen Tannenbaum
wie folgt ausgibt:
	     *
	    ***
	   *****
	  *******
	 *********
	***********
	    ***
	    ***
	    ***
'''
for i in range(6):
    for j in range(6 - i - 1):
       print(" ",end="")
    for j in range(2*i+1):
       print("*",end="")
    print()     #Zeilenumbruch
for i in range(3):
    for i in range(4):
        print(" ",end="")
    for i in range(3):
        print("*",end="")
    print()     #Zeilenumbruch    
        
        
print("Nur bei Python","-"*10)
                   
for i in range(6):
       print(" "*(6-i-1),end="")
       print("*"*(2*i+1))
for i in range(3):
    print(" "*4,end="")
    print("*"*3)
       
       
