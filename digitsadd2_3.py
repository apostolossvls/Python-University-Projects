print("*Gives amount of numbers (of N digits) that their ascending digits adds to a Sum(S)*")
n = int(input("Give number of digits 'N' (from 1 to 9 'for obvious reasons'): "))
while (n<1 or n>9):
	n = int(input("Give number of digits 'N' (from 1 to 9 'for obvious reasons'): "))
s = int(input("Give number of digits 'S' (from 1 to 45 'for obvious reasons'): "))
while (s<1 or s>45):
	s = int(input("Give number of digits 'S' (from 1 to 45 'for obvious reasons'): "))
c=0
def loop(s,start,dig,maxdig,c):
	flag = 0
	i=start
	while i < 10 and flag==0:
		if i==s:
			flag=1
		elif dig < maxdig:
			c = loop(s-i,i+1,dig+1,maxdig,c)
		i=i+1
	if flag==1:
		c=c+1
	return c
c = loop(s,1,1,n,c)
print("Amount of numbers that their digits adds to S: "+str(c))