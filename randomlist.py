import random
print ('*Gives all combinations of 30 numbers (from -30 to 30) that adds to 0*')
print (32*"-")
randomlist = []
for i in range(30):
	randomlist.append(random.randint(-30, 30))
print("Your random numbers: " + str(randomlist))
flag=0
loop=0
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
								loop=loop+1
								listw.append(randomlist[w])
								print (str(randomlist[i])+" , "+str(randomlist[j])+" , "+str(randomlist[w]))
								flag = 1
								fi=1
								fj=1
					if fj==1:
						listj.append(randomlist[j])
		if fi==1:
			listi.append(randomlist[i])
print (32*"-")
if flag==0:
	print("There is not a single pack of 3 numbers that adds to 0. You are very unlucky or the luckiest man in the world")
print("Amount of found combinations:" + str(loop))
#print("Max combinations: "+str(30*30*30))
