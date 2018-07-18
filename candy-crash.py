lis=[]
with open("candy_input1.txt", "r") as f:
	for line in f:
		lis2=[]
		#After reading the data for each line of the file, remove \n and split  into the lis string.
		for i in line.strip().split(","): 
			lis2.append(int(i))
		lis.append(lis2)

wide=len(lis[0])
height=len(lis)
while True:
	#Find out more than three numbers in each horizontal row. If the conditions are true → negative sign
	#Horizontal row
	convert=False	
	for i in range(height):
		l,r=0,0
		while r<wide:
			while lis[i][r]==lis[i][l]: #If the values ​​of the two parameters are the same, the indicator is shifted to the right by one grid.
				r+=1
				if r>wide-1: #Break beyond the width
					break
			if r-1>=3:
				if lis[i][l]: #There are consecutive 0s, but 0 is not counted in the things to be erased.
					convert=True
				lis[i][l:r]=[-j for j in lis[i][l:r]] #Change the same to a negative sign
			l=r

	#straight row
	for i in range(wide):
		u,d=0,0
		while d<height:  #Same as Horizontal row
			while abs(lis[d][i])==abs(lis[u][i]):
				d+=1
				if d>height-1:
					break
			if d-u>=3:
				if lis[u][i]:
					convert=True
				while u<d:
					lis[u][i]=-abs(lis[u][i])
					u+=1
			u=d

	#Make up 0
	for i in range(wide):
		u=d=height-1
		while u>=0:
			if lis[u][i]>0:	#<0→erased
				lis[d][i]=lis[u][i]
				d-=1
			u-=1

		#After the elimination, make up 0
		while d>=0:
			lis[d][i]=0
			d-=1
	if not convert:
		break
print(lis)

#Write the file
with open("candy_output.txt", "w") as f:
	for i in range(height):
		change=True
		for j in range(wide):
			if not change:
				f.write(",")
			change=False
			f.write(str(lis[i][j]))
		f.write("\n")

