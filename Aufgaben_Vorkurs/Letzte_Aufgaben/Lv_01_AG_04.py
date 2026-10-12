'''AufgabeTag14_L1_4
 

'''
liste = []   #liste braucht man hier nicht
for i in range (51,70):
    liste.append(i)
    if i%3 ==1 :
        i += 100
    print(i, end= " ")

print("\n"+'_'*50)

#2Variant
for i in range (51,70):
    if i%3 ==1 :
        i += 100
    print(i, end= " ")
