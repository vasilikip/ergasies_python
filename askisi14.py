#������ 14

"""�������� ������� ��� ��� ������ �����������
�� a ������� ��� ���� ����������� ��� b �� ����� ��� ����������� ��� c ���� ������ ��� �������� [a,b]"""

a= int(input("���� ���� ������: "))
while True:
	b=int(input("���� ����� ���� ������ ���������� ��� a: "))
	if b>a:
		break
		
while True:
	c=int(input("���� ���� ������ ��������� ��� b: "))
	if c<b:
		break
#���������� ������ �� ���� �������� ��� ��������[a,b]		
lista=[]
for i in range((b-a)+1):
	lista.append(a)
	a+=1
	

#��������� ��� ������� �� ����� ������ �������
def first(num):
	for i in range(2,num):
		if num%i==0:
			num=0
			break
	return num	
			


"""� �������� ������� ������� �� �������� ��� ������ ����� �� ���� �� ����� ������ 
����� ������� ��� �� ������ c=|p-q|"""
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
	print("��� ������� �������� ����� ������� �� ����� ���� ������� ��� ��:")
	print(c)
else:
	print(p,q)
 
	
