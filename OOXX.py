#Game:Tic‐Tac‐Toe 
#==================================================================
print(" 1 | 2 | 3 \n---|---|---\n 4 | 5 | 6 \n---|---|---\n 7 | 8 | 9 \n")
print("   |   |   \n---|---|---\n   |   |   \n---|---|---\n   |   |   \n")

#Use string to represent the result of each input update
x=" %s | %s | %s \n---|---|---\n %s | %s | %s  \n---|---|---\n %s | %s | %s \n"
lis=[" "," "," "," "," "," "," "," "," "]

i=1
while 1<=i<=9:	
	while i%2!=0: #Change player O input
		A=int(input("(O)Slect [1~9]:"))
		if A<1 or A>9: #Input is illegal
			print("Invalid input.Try again.")
		elif lis[A-1]!=" ": #The grid has been filled
			print("Cell",A,"has been filled.Try again.")		
		else:
			lis[A-1]=0 #O
			print(x%(lis[0],lis[1],lis[2],lis[3],lis[4],lis[5],lis[6],lis[7],lis[8]))
			#List the possibilities for each win
			if lis[0]==lis[1]==lis[2]==0 or lis[3]==lis[4]==lis[5]==0 or lis[6]==lis[7]==lis[8]==0 or lis[0]==lis[4]==lis[8]==0 or lis[2]==lis[4]==lis[6]==0 or lis[0]==lis[3]==lis[6]==0 or lis[1]==lis[4]==lis[7]==0 or lis[2]==lis[5]==lis[8]==0:
				print("Player O win!")
			#Flat
			elif i==9:
				print(x%(lis[0],lis[1],lis[2],lis[3],lis[4],lis[5],lis[6],lis[7],lis[8]))
				print("Tie Bye~")
			i+=1
									
	while i%2==0:  #Change player X input
		B=int(input("(X)Slect [1~9]:"))	 	
		if B<1 or B>9: #Input is illegal
			print("Invalid input.Try again.")
		elif lis[B-1]!=" ": #The grid has been filled
			print("Cell",B,"has been filled.Try again.")				
		else:
			lis[B-1]="X" #X
			print(x%(lis[0],lis[1],lis[2],lis[3],lis[4],lis[5],lis[6],lis[7],lis[8]))
			#List the possibilities for each win
			if lis[0]==lis[1]==lis[2]=="X" or lis[3]==lis[4]==lis[5]=="X" or lis[6]==lis[7]==lis[8]=="X" or lis[0]==lis[4]==lis[8]=="X" or lis[2]==lis[4]==lis[6]=="X" or lis[0]==lis[3]==lis[6]=="X" or lis[1]==lis[4]==lis[7]=="X" or lis[2]==lis[5]==lis[8]=="X":
				print("Player X win!")			
			i+=1	
	
