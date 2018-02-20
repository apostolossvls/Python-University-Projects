import datetime
print ('Date Coincidence?!')
today = datetime.date.today()
w = today.weekday()
if w == 0: wstr = "Monday"
elif w == 1: wstr = "Tuesday"
elif w == 2: wstr = "Wednesday"
elif w == 3: wstr = "Thursday"
elif w == 4: wstr = "Friday"
elif w == 5: wstr = "Saturday"
elif w == 6: wstr = "Sunday"
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
s=""
if c>1:
	s="s"
print("This day on this month happens to be "+wstr+" `"+ str(c)+"` more time"+s+" the next 10 years")
