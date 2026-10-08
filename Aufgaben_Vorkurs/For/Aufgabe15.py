'''
Aufgabe for.15
Entwickeln Sie ein Programm mit Schleifen, das einen Tannenbaum wie folgt ausgibt:
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

#Herr Adams
#لازم نطبع فقط النجمات وليس يلي بعدها
for i in range (6):
    for j in range (6-i-1):
       print(" " , end = '')
    for j in range (2*i+1):
        print("*" ,end ='')
    print()    
for i in range(3):
    for i in range(4):
        print(" ",end="")
    for i in range(3):
        print("*",end="")
    print()     #Zeilenumbruch    
        


print("-" * 20)

for i in range (6):
    print(' ' * (6-i-1), end ='')
    print ('*' * (2*i + 1))
for a in range (3):
    for b in range (11):
        if 3< b < 7:
            print ('*',end ='')
        else:
            print (' ',end ='')
    print()

    
