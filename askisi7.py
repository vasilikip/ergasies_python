#������ 7


import random
#���������� ���� �������
table={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
#��������� ��� ��������� �� ������ ��� �������� ���� �����
def game(table):
	print(table[1]+"|"+table[2]+"|"+table[3])
	print("-+-+-")
	print(table[4]+"|"+table[5]+"|"+table[6])
	print("-+-+-")
	print(table[7]+"|"+table[8]+"|"+table[9])
	
game(table)	
#�������� �������� ��� ��� ������
while True:
	shape=input("������� ��� ����� � � �: ")
	if shape=="X" or shape=="O":
		break
if shape=="X":
        shape1="O"
else:
        shape1="X"
"""�� �������� �� ���������� ����� ����� ����� ��� �� ������� ����� ��� ��������� ��� ��������"""
for i in range(9):
        game(table)
        if i%2==0:
                while True:
                        m=int(input("������� ��� ����: "))
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
                        print("��������!")
			
                else:
                        print("������.")
                break
				
        if table[4]==table[5]==table[6]=="X" or table[4]==table[5]==table[6]=="O" :
                if table[4]==shape:
                        print("��������!")
                        break
                else:
                        print("������.")
                        break
        if table[7]==table[8]==table[9]=="X" or table[7]==table[8]==table[9]=="O":
                if table[7]==shape:
                        print("��������!")
                        break
                else:
                        print("������.")
                        break
        if table[1]==table[4]==table[7]=="X" or table[1]==table[4]==table[7]=="O" :
                if table[1]==shape:
                        print("��������!")
                        break
                else:
                        print("������.")
                        break
        if table[2]==table[5]==table[8]=="X" or table[2]==table[5]==table[8]=="O":
                if table[2]==shape:
                        print("��������!")
                        break
                else:
                        print("������.")
                        break
        if table[3]==table[6]==table[9]=="X" or table[3]==table[6]==table[9]=="O" :
                if table[3]==shape:
                        print("��������!")
                        break
                else:
                        print("������.")
                        break
        if table[1]==table[5]==table[9]=="X" or table[1]==table[5]==table[9]=="O" :
                if table[1]==shape:
                        print("��������!")
                        break
                else:
                        print("������.")
                        break
        if table[3]==table[5]==table[7]=="X" or table[3]==table[5]==table[7]=="O" :
                if table[3]==shape:
                        print("��������!")
                        break
                else:
                        print("������.")
                        break
        
                
	

