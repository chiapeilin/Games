#Game:Determine whether it is a leap year and count the number of days
#======================================================================
#Input the date
date=input("Input a date(yyyy/mm/dd):")
yyyy=date[:4]
mm=date[5:7]
dd=date[8:]
year=int(yyyy)
month=int(mm)
day=int(dd)

#Determine if the input is legal
if year>=0:
	if year%4==0 and year%100==0 and year%400==0:
		if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
			if 1<=day<=31:
				print("Yes!The date is valid.")
			if not 1<=day<=31:
				print("Day Invalid")
		elif month==4 or month==6 or month==9 or month==11:
			if 1<=day<=30:
				print("The date is valid.")
			if not 1<=day<=30:
				print("Day Invalid")
		elif month==2:
			if 1<=day<=29:
				print("The date is valid.")
			if not 1<=day<=29:
				print("Day Invalid")
		
	if year%4==0 and year%100==0 and year%400!=0:
		if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
			if 1<=day<=31:
				print("The date is valid.")
			if not 1<=day<=31:
				print("Day Invalid")
		elif month==4 or month==6 or month==9 or month==11:
			if 1<=day<=30:
				print("The date is valid.")
			if not 1<=day<=30:
				print("Day Invalid")
		elif month==2:
			if 1<=day<=28:
				print("The date is valid.")
			if not 1<=day<=28:
				print("Day Invalid")
		
	if year%4==0 and year%100!=0 :
		if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
			if 1<=day<=31:
				print("The date is valid.")
			if not 1<=day<=31:
				print("Day Invalid")
		elif month==4 or month==6 or month==9 or month==11:
			if 1<=day<=30:
				print("The date is valid.")
			if not 1<=day<=30:
				print("Day Invalid")
		elif month==2:
			if 1<=day<=29:
				print("The date is valid.")
			if not 1<=day<=29:
				print("Day Invalid")
		
	elif year%4!=0:
		if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
			if 1<=day<=31:
				print("The date is valid.")
			if not 1<=day<=31:
				print("Day Invalid")
		elif month==4 or month==6 or month==9 or month==11:
			if 1<=day<=30:
				print("The date is valid.")
			if not 1<=day<=30:
				print("Day Invalid")
		elif month==2:
			if 1<=day<=28:
				print("The date is valid.")
			if not 1<=day<=28:
				print("Day Invalid")
else:
	print("Year Invalid")


if not 1<=month<=12:
	print("Month Invalid.")

if  (not 1<=month<=12) and not 1<=day<=31:
	print("Day Invalid.")

#Determine whether it is a leap year and count the number of days
count_day=0
if (year%4==0 and(not year%100==0 or year%400==0)) and month==1 and 1<=day<=31:
	count_day=day
elif (year%4==0 and(not year%100==0 or year%400==0)) and month==2 and 1<=day<=29:	
	count_day=31+day
elif (year%4==0 and(not year%100==0 or year%400==0)) and month==3 and 1<=day<=31:
	count_day=31+29+day
elif (year%4==0 and(not year%100==0 or year%400==0)) and month==4 and 1<=day<=30:
	count_day=31+29+31+day
elif (year%4==0 and(not year%100==0 or year%400==0)) and month==5 and 1<=day<=31:
	count_day=31+29+31+30+day
elif (year%4==0 and(not year%100==0 or year%400==0)) and month==6 and 1<=day<=30:
	count_day=31+29+31+30+31+day
elif (year%4==0 and(not year%100==0 or year%400==0)) and month==7 and 1<=day<=31:
	count_day=31+29+31+30+31+30+day		
elif (year%4==0 and(not year%100==0 or year%400==0)) and month==8 and 1<=day<=31:
	count_day=31+29+31+30+31+30+31+day
elif (year%4==0 and(not year%100==0 or year%400==0)) and month==9 and 1<=day<=30:			
	count_day=31+29+31+30+31+30+31+31+day		
elif (year%4==0 and(not year%100==0 or year%400==0)) and month==10 and 1<=day<=31:
	count_day=31+29+31+30+31+30+31+31+30+day
elif (year%4==0 and(not year%100==0 or year%400==0)) and month==11 and 1<=day<=30:
	count_day=31+29+31+30+31+30+31+31+30+31+day
elif (year%4==0 and(not year%100==0 or year%400==0)) and month==12 and 1<=day<=31:
	count_day=31+29+31+30+31+30+31+31+30+31+30+day
else:
	count_day=0

if (not(year%4==0 and(not year%100==0 or year%400==0)))and month==1 and 1<=day<=31:
	count_day=day
elif(not(year%4==0 and(not year%100==0 or year%400==0))) and month==2 and 1<=day<=28:	
	count_day=31+day
elif (not(year%4==0 and(not year%100==0 or year%400==0))) and month==3 and 1<=day<=31:
	count_day=31+28+day
elif (not(year%4==0 and(not year%100==0 or year%400==0))) and month==4 and 1<=day<=30:
	count_day=31+28+31+day
elif (not(year%4==0 and(not year%100==0 or year%400==0))) and month==5 and 1<=day<=31:
	count_day=31+28+31+30+day
elif (not(year%4==0 and(not year%100==0 or year%400==0))) and month==6 and 1<=day<=30:
	count_day=31+28+31+30+31+day
elif (not(year%4==0 and(not year%100==0 or year%400==0))) and month==7 and 1<=day<=31:
	count_day=31+28+31+30+31+30+day		
elif (not(year%4==0 and(not year%100==0 or year%400==0))) and month==8 and 1<=day<=31:
	count_day=31+28+31+30+31+30+31+day
elif (not(year%4==0 and(not year%100==0 or year%400==0))) and month==9 and 1<=day<=30:			
	count_day=31+28+31+30+31+30+31+31+day		
elif (not(year%4==0 and(not year%100==0 or year%400==0))) and month==10 and 1<=day<=31:
	count_day=31+28+31+30+31+30+31+31+30+day
elif (not(year%4==0 and(not year%100==0 or year%400==0))) and month==11 and 1<=day<=30:
	count_day=31+28+31+30+31+30+31+31+30+31+day
elif (not(year%4==0 and(not year%100==0 or year%400==0))) and month==12 and 1<=day<=31:
	count_day=31+28+31+30+31+30+31+31+30+31+30+day

#Print the result
if count_day!=0:
	print(date,"is the No.",count_day,"day of the year.")
