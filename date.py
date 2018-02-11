import datetime
print ('Date Coincidence?!')
today = datetime.date.today()
w = today.weekday()
if w == 0: wstr = "deutera"
elif w == 1: wstr = "trith"
elif w == 2: wstr = "tetarth"
elif w == 3: wstr = "pempth"
elif w == 4: wstr = "paraskeuh"
elif w == 5: wstr = "sabbato"
elif w == 6: wstr = "kuriakh"
y = today.year + 1
m = today.month
d = today.day
print ("Today: " +str(today)+ " " +wstr)
c=0
for i in range(10):
	testdate = datetime.date(y, m, d)
	if testdate.weekday() == w:
		c=c+1
	y=y+1
	testdate = datetime.date(y, m, d)
print("Same weekday in the next 10 years: "+ str(c))