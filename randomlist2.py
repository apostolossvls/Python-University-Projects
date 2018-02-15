import random
print ("*Gives all 3-numbered groups from 30 random numbers (from -30 to 30) that adds to 0*")
cond = int(input("Output (1)all combination (2)without duplicates (3)both ('1' or '2' or '3'): "))
while (cond!=1 and cond!=2 and cond!=3):
	cond = int(input("Output (1)all combination (2)without duplicates (3)both ('1' or '2' or '3'): "))
print (42*"-")
randomlist = []
for i in range(30):
	randomlist.append(random.randint(-30, 30))
print("Your random numbers: " + str(randomlist))
print (42*"-")
flag=0
numlist=[]
listi=[]
for i in range(len(randomlist)):
	if randomlist[i] not in listi:
		fi=0
		listj=[]
		for j in range(len(randomlist)):
			if randomlist[j] not in listj:
				fj=0
				listw=[]
				if randomlist[i] + randomlist[j] >= -30 or randomlist[i] + randomlist[j] <= 30:
					for w in range(len(randomlist)):
						if randomlist[w] not in listw:
							if randomlist[i] + randomlist[j] + randomlist[w] == 0:
								listw.append(randomlist[w])
								numlist.append([randomlist[i],randomlist[j],randomlist[w]])
								flag=1
								fi=1
								fj=1
					if fj==1:
						listj.append(str(randomlist[j]))
		if fi==1:
			listi.append(randomlist[i])
if flag==0:
	print("There is not a single pack of 3 numbers that adds to 0. You are very unlucky or the luckiest man in the world")
else:
	if cond>=2:
		if cond==3:
			cond=1
		finallist=[]
		for group in numlist:
			if not finallist:
				finallist.append(group)
			else:
				f=0
				for fg in finallist:
					bc=0
					for i in range(3):
						if group[i] in fg:
							bc+=1
					if bc>1:
						f=1
				if f==0:
					finallist.append(group)
		f=0
		for i in randomlist:
			if i==0:
				finallist.append([0,0,0])
				f=1
				break
		print("Your numbers without duplicates")
		print (finallist)
		print (32*"-")
		if f==0:
			print ("Amount: "+str(len(finallist)))
		else: 
			print ("Amount: "+str(len(finallist))+" or "+str(len(finallist)-1)+" without counting [0,0,0]")
		if cond==1:
			print (42*"-")
	if cond==1:
		print ("Your numbers with all combinations")
		print (numlist)
		print (32*"-")
		print ("Amount: "+str(len(numlist)))
