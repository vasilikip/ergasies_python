#������ 3

#�������� �������� ������� ��� ��� ������
name=input("���� ����� �������: ")
#������� ������� ��� ����� � ������� ��� �������� ��� ������� ���� ������� ��� ��������

myfile=open(name,'r')
myfile1=open('file2.txt','w')

#��� ������ ��� ������� �� �������� �� ������ ��� ������ ����� �� ������
content=''
for line in myfile:
	l=''
	if line[0]!="#":
		content=content+line


print('������� ����� ������:')
print(content)
myfile1.write(content)
	

