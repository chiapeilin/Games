#Game:Rock‐Paper‐Scissors 
#==================================================================
myformat="%-15s%-15s%-15s"
print(myformat%("Player A","Player B","Result"))
print(myformat%("Rock","Rock","Tie"))
print(myformat%("Rock","Paper","Player B"))
print(myformat%("Rock","Scissors","Player A"))
print(myformat%("Paper","Rock","Player A"))
print(myformat%("Paper","Paper","Tie"))
print(myformat%("Paper","Scissors","Player B"))
print(myformat%("Scissors","Rock","Player B"))
print(myformat%("Scissors","Paper","Player A"))
print(myformat%("Scissors","Scissors","Tie"))

while  True:
	print("Please enter rock or paper or scissors or bye.")

	a=input("Player A? ")
	#Determine if the input is legal
	while a!="paper" and a!="scissors" and a!="rock" and a!="bye":
		print("Invalid input. Please enter again.")	
		a=input("Player A? ")
	if a=="bye":
		break

	b=input("Player B? ")
	#Determine if the input is legal
	while b!="paper" and b!="scissors" and b!="rock" and b!="bye":
		print("Invalid input. Please enter again.")	
		b=input("Player B? ")
	if b=="bye":
		break

	#Determine who wins
	if a=="rock" and b=="rock":
		print(a,b)
		print("Outcome:Tie")
	elif a=="rock" and b=="paper":
		print(a,b)
		print("Outcome:Player B wins!")
	elif a=="rock" and b=="scissors":
		print(a,b)
		print("Outcome:Player A wins!")

	elif a=="paper" and b=="rock":
		print(a,b)
		print("Outcome:Player A wins!")
	elif a=="paper" and b=="paper":
		print(a,b)
		print("Outcome:Tie")
	elif a=="paper" and b=="scissors":
		print(a,b)
		print("Outcome:Player B wins!")

	elif a=="scissors" and b=="rock":
		print(a,b)
		print("Outcome:Player B wins!")
	elif a=="scissors" and b=="paper":
		print(a,b)
		print("Outcome:Player A wins!")
	elif a=="scissors" and b=="scissors":
		print(a,b)
		print("Outcome:Tie")
	print()

