#Game:21-points
#=====================================================
while 1:
	import random
	ranks=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
	suits=['Club','Diamond','Heart','Spade']
	#make a deck of cards
	deck=[]
	for i in suits:
		for j in ranks:
			deck.append(j+"-"+i)
	random.shuffle(deck)
	#Player draws two cards
	hand=[deck[0],deck[1]]  
	deck.pop(0)
	deck.pop(0)
	#Separate numbers from suits
	number=[]
	for card in hand:
		card1=card.split("-")
		number+=[card1[0]]
	#compute current value
	total=0
	for i in range(len(number)):
		if number[i]=="J" or number[i]=="Q" or number[i]=="K":
			total+=10
		elif number[i]=="A":
			total+=11
		else:
			total+=int(number[i])
	#Determine if it is 21 points
	if total==21:
		print("Your value is Blackjack! (21)")
	print("Your current value is",total)		
	print("with the hand: "+", ".join(hand)+"\n")

	n=0
	while True and total<=21:
		c=input("Hit or stay?(Hit = 1, Stay = 0):")
		print()
		if c=="0":
			break
		#Draw another card
		if c=="1":
			n+=1			
			hand_1=deck[0]
			deck.pop(0)  
			print("Your draw:"+hand_1+"\n")
			hand.append(hand_1)
			#Separate numbers from suits
			hand_2=hand_1.split("-")		
			number_1=[]
			number_1+=[hand_2[0]]
			hand_1=[]
			#compute current value
			if number_1[0]=="J" or number_1[0]=="Q" or number_1[0]=="K":
				total+=10
			elif number_1[0]=="A":
				total+=11
			else:
				total+=int(number_1[0])
			#Print the result
			if total<21:
				if total>21 and card.count("A")!=0:
					total-=10			
				print("Your current value is",total)
				print("with the hand: "+", ".join(hand)+"\n")
			if total>21:
				print("Your current value is Bust!(>21)")
				print("with the hand: "+", ".join(hand)+"\n")
				break
			if total==21:
				print("Your value is Blackjack! (21)")
				print("with the hand: "+", ".join(hand)+"\n")
				break		
	#----------------------------------------------------------------------------		
	#The dealer draws two cards
	hand_d=[deck[0],deck[1]]
	deck.pop(0)
	deck.pop(0)
	#Separate numbers from suits
	number_d=[]
	for card_d in hand_d:
		card_d1=card_d.split("-")
		number_d+=[card_d1[0]]
	#compute current value
	total_d=0
	for i in range(len(number_d)):
		if number_d[i]=="J" or number_d[i]=="Q" or number_d[i]=="K":
			total_d+=10
		elif number_d[i]=="A":
			total_d+=11
		else:
			total_d+=int(number_d[i])
	#Determine if it is 21 points
	if total_d==21:
		print("Dealer's value is Blackjack! (21)")
	print("Dealer's current value is",total_d)		
	print("with the hand: "+", ".join(hand_d)+"\n")

	n1=0
	while True and total_d<=17:
		if total_d>21:
			break
		#Draw another card
		if total_d<=17:
			n1+=1			
			hand_d1=deck[0]
			deck.pop(0)   
			print("Dealer draw:"+hand_d1+"\n")
			hand_d.append(hand_d1)
			#Separate numbers from suits
			hand_d2=hand_d1.split("-")		
			number_d1=[]
			number_d1+=[hand_d2[0]]
			hand_d1=[]
			#Compute current value
			if number_d1[0]=="J" or number_d1[0]=="Q" or number_d1[0]=="K":
				total_d+=10
			elif number_d1[0]=="A":
				total_d+=11
			else:
				total_d+=int(number_d1[0])
			#Print the result
			if total_d<21:
						
				print("Dealer's current value is",total_d)
				print("with the hand: "+", ".join(hand_d)+"\n")
			if total_d>21:
				if total_d>21 and card_d.count("A")!=0:
					total_d-=10*count("A")	
				print("Dealer's current value is Bust!(>21)")
				print("with the hand: "+", ".join(hand_d)+"\n")
				break
			if total_d==21:
				print("Dealer's value is Blackjack! (21)")
				print("with the hand: "+", ".join(hand_d)+"\n")
				break
	#Judge the winner
	if total==21 and total_d!=21:
		print("****You beat the dealer !****")
	elif total_d==21 and total!=21:
		print("****Dealer wins !****")
	elif total>21 and total_d<=21:
		print("****Dealer wins !****")
	elif total<=21 and total_d>21:
		print("****You beat the dealer !****")
	elif total>21 and total_d>21:
		print("****You tied the dealer. Nobody wins.****")
	elif total==21 and total_d==21:
		print("****You tied the dealer. Nobody wins.****")
	elif total==total_d:
		print("****You tied the dealer. Nobody wins.****")
	elif total<21 and total_d<21:
		if total>total_d:
			print("****You beat the dealer !****")
		elif total<total_d:
			print("****Dealer wins !****")
	#The game has to continue?
	again=input("Want to piay again? (y/n): ")
	if again=="y":
		print("---------------------------------------------")
		print()
		continue
	if again=="n":
		break
