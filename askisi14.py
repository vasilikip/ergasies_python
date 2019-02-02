#ασκηση 14

"""Εισαγώγη αριθμών για την δέλωση διαστήματος
το a δηλώνει την αρχή διαστήματος και b το τέλος του διαστήματος και c έναν αριθμό στο δίαστημα [a,b]"""

a= int(input("Δώσε έναν αριθμό: "))
while True:
	b=int(input("Δώσε ακόμα έναν αριθμό μεγαλύτερο του a: "))
	if b>a:
		break
		
while True:
	c=int(input("Δώσε έναν αριθμό μικρότερο του b: "))
	if c<b:
		break
#δημιουργία λίστας με τους αριθμούς στο δίαστημα[a,b]		
lista=[]
for i in range((b-a)+1):
	lista.append(a)
	a+=1
	

#συνάρτηση που ελέγχει αν ειναι πρώτος αριθμός
def first(num):
	for i in range(2,num):
		if num%i==0:
			num=0
			break
	return num	
			


"""Ο παρακάτω κάδικας ελέγχει τα στοιχεία της λίστας μέχρι να βρει το πρώτο ζεύγος 
πώτων αριθμών που να ισχύει c=|p-q|"""
d=len(lista)-1
for i in range(d):
	for j in range(i,d):
		num1=lista[i]
		num2=lista[j+1]
		if lista[j+1]-lista[i]==c:
			break
	p=first(num1)
	q=first(num2)
	if p!=0 and q!=0:
		break
		
if p==0 and q==0:
	print("δεν υπάρχει διάστημα πώτων αριθμών το οποίο έχει διαφορά ίση με:")
	print(c)
else:
	print(p,q)
 
	
