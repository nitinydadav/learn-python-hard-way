p = (1,2,3,4,5,6,7,9,)


def one(items):
	even = []
	odd = []
	for q in items:
		if (q%2 ==0):
			even.append(q)
		else:
			odd.append(q)
	return even, odd

print one(p)	 
		
