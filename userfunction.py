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

print (one(p))
		

print ("\n")
# reverse string 
p = ["fun", "to", "time", "it's", "bosko","hello"]                                  

def file(p):	
	p.reverse()
	return p
print (file(p))

print ("\n")



#variable length  argument 
def file(*one):
	print(one[0])
	print(one[1])
	print(one[2])
	z = one[0] + one[1] + one [2]
	return ("this is the sum:", (z))
print(file (2,5,8,))

	
print("\n")


def file1(x, *one):
	w = x * one[0] * one [1]

	return ("multiply:",w)
 
print(file1(8,2,4))
