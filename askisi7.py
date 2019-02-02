#ΑΣΚΗΣΗ 7


import random
#δημιουργία ενός λεξικού
table={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
#Συνάρτηση που εμφανίζει το πίνακα της τρίλιζας στην οθόνη
def game(table):
	print(table[1]+"|"+table[2]+"|"+table[3])
	print("-+-+-")
	print(table[4]+"|"+table[5]+"|"+table[6])
	print("-+-+-")
	print(table[7]+"|"+table[8]+"|"+table[9])
	
game(table)	
#Εισαγωγή συμβόλου από τον χρήστη
while True:
	shape=input("Διάλεξε ένα σχήμα Χ ή Ο: ")
	if shape=="X" or shape=="O":
		break
if shape=="X":
        shape1="O"
else:
        shape1="X"
"""Το παιχνίδι θα εκτελεστεί εννια φορές εκτός και αν καποιος κάνει τον συνδυασμό που κερδίζει"""
for i in range(9):
        game(table)
        if i%2==0:
                while True:
                        m=int(input("Διάλεξε ένα κελί: "))
                        if table[m]==' ':
                                table[m]=shape
                                break
        else:
                print("\n")
                while True:
                        m=random.randint(1,9)
                        if table[m]==' ':
                                table[m]=shape1
                                break
        if table[1]==table[2]==table[3]=="X" or table[1]==table[2]==table[3]=="O" :
                if table[1]==shape:
                        print("Κερδισες!")
			
                else:
                        print("Έχασες.")
                break
				
        if table[4]==table[5]==table[6]=="X" or table[4]==table[5]==table[6]=="O" :
                if table[4]==shape:
                        print("Κερδισες!")
                        break
                else:
                        print("Έχασες.")
                        break
        if table[7]==table[8]==table[9]=="X" or table[7]==table[8]==table[9]=="O":
                if table[7]==shape:
                        print("Κερδισες!")
                        break
                else:
                        print("Έχασες.")
                        break
        if table[1]==table[4]==table[7]=="X" or table[1]==table[4]==table[7]=="O" :
                if table[1]==shape:
                        print("Κερδισες!")
                        break
                else:
                        print("Έχασες.")
                        break
        if table[2]==table[5]==table[8]=="X" or table[2]==table[5]==table[8]=="O":
                if table[2]==shape:
                        print("Κερδισες!")
                        break
                else:
                        print("Έχασες.")
                        break
        if table[3]==table[6]==table[9]=="X" or table[3]==table[6]==table[9]=="O" :
                if table[3]==shape:
                        print("Κερδισες!")
                        break
                else:
                        print("Έχασες.")
                        break
        if table[1]==table[5]==table[9]=="X" or table[1]==table[5]==table[9]=="O" :
                if table[1]==shape:
                        print("Κερδισες!")
                        break
                else:
                        print("Έχασες.")
                        break
        if table[3]==table[5]==table[7]=="X" or table[3]==table[5]==table[7]=="O" :
                if table[3]==shape:
                        print("Κερδισες!")
                        break
                else:
                        print("Έχασες.")
                        break
        
                
	

