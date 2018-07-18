#Find the 20 players with the highest 20 career efficiency scores
#================================================================
data,lis=[],[]

#Each line of data after reading \n is removed and stored in the data string.
with open("nba_data.csv","r") as nba_data:
	for line in nba_data:
		data.append(line.strip())
	#(Hive string) divides each row in Data into splits and adds them to the lis string.
	for l in range(len(data)):
		lis.append(data[l].split(","))

#Compute the most efficient season
year_name,sum,eff_season=[],[],[]
count_1=1

for i in range(1,len(lis)):
	#Determine if player data has appeared
	if [lis[i][1],lis[i][2],lis[i][3]] not in year_name:
		year_name.append([lis[i][1],lis[i][2],lis[i][3]])
		sum.append(lis[i])
	
	else: #[lis[i][0],lis[i][1]] in year_name		
		w=year_name.index([lis[i][1],lis[i][2],lis[i][3]])

		for a in range(5,17):
			sum[w][a]=str(int(sum[w][a])+int(lis[i][a]))

#Add the same season data of the same player
for i in range(len(sum)):
	eff_season.append(((int(sum[i][7])+int(sum[i][8])+int(sum[i][9])+int(sum[i][10])+int(sum[i][11]))-((int(sum[i][13])-int(sum[i][14]))+(int(sum[i][15])-int(sum[i][16]))+int(sum[i][12])))/int(sum[i][5]))

#Compute the most efficient career
player,eff,count=[],[],[]
for i in range(len(eff_season)):
	#Determine if player data has appeared
	if [year_name[i][1:]] not in player:
		player.append([year_name[i][1:]])
		eff.append(eff_season[i])
		count.append(1)
	else:
		r=player.index([year_name[i][1:]])
		eff[r]=eff_season[i]+eff[r]
		count[r]+=1
#Add all the information of the same player
eff_career=[]
for i in range(len(eff)):
	eff_career.append([eff[i]/count[i],player[i]])
#Sort by player efficiency from high to low
eff_career.sort() 
eff_career=eff_career[::-1]

#Print the rankings and write to the notebook
output=open("nba_best.txt","w")
for i in range(0,20):	
	name=" ".join(eff_career[i][1][0])
	print("Rank%d\t%-20s\t%.2f"%(i+1,name,eff_career[i][0]))
	output.write("Rank%d\t%-20s\t%.2f\n"%(i+1,name,eff_career[i][0]))		
output.close()

