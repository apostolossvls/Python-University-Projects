print ('ROT13')
txt = input("Give text : ")
tl = list(txt)
c=0
for ch in tl:
	if (ch>='a' and ch<='m') or (ch>='A' and ch<='M'):
		tl[c] = chr(ord(ch)+13)
	elif (ch>='n' and ch<='z') or (ch>='N' and ch<='Z'):
		tl[c] = chr(ord(ch)-13)
	c=c+1
txt = "".join(tl)
print ("Your modified text: " + txt)