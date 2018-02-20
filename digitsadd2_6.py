print("*Gives amount of numbers (of N digits) that their rising digits adds to a Sum(S)*")
n = int(input("Give number of digits 'N': "))
while (n<1):
	n = int(input("Give number of digits 'N': "))
s = int(input("Give number of digits 'S': "))
while (s<1):
	s = int(input("Give number of digits 'S': "))
c=0
def loop(s,start,dig,c):
	flag = 0
	i=start
	while i < 10 and flag==0:
		if i==s:
			flag=1
		elif dig < n:
			c = loop(s-i,i,dig+1,c)
		i=i+1
	if flag==1:
		#print((dig-1)*"#"+str(i-1))
		c=c+1
	return c
c = loop(s,1,1,c)
#for i in range(1,10):
#	for j in range(2,n+1):
#		if j*i==s:
#			c-=1
#deleted calc that excluded numbers like 11,222,777,99999 as they count on the problem
print("Amount of numbers that their rising digits adds to S: "+str(c))
