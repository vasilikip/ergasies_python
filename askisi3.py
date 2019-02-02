#ΑΣΚΗΣΗ 3

#εισαγωγή ονόματος αρχείου απο τον χρήστη
name=input("Δώσε όνομα αρχείου: ")
#άνοιγμα αρχείου που έδωσε ο χρήστης για ανάγνωση και ανοιγμα ενός αρχέιου για εγγγραφη

myfile=open(name,'r')
myfile1=open('file2.txt','w')

#στο αρχείο για εγγραφή θα γράψουμε το αρχειο του χρήστη χωρίς τα σχόλια
content=''
for line in myfile:
	l=''
	if line[0]!="#":
		content=content+line


print('Κώδικας χωρίς σχόλια:')
print(content)
myfile1.write(content)
	

