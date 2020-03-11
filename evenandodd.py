items = [2,3,4,5,6,7,8,9]

odd = []
even = []

for num in items:
	if num%2== 0:
		even.append(num)
	else:
		odd.append(num) 

print "items:   ", items 
print "even:   ", even
print "odd:    ", odd  
