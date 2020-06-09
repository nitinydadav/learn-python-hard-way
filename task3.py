items_1 = [{"name": "naveen", "age": 12}, {"name": "nitin", "age": 16}, {"name": "ritu", "age": 23}]


for q in items_1:
	q.values()
	print(q.values())

print ("\n")
q = []
for w in items_1:
     x = w.values()
     q.extend(x)
print(q)

z = []
for q in items_1:
	w =  q["age"]
	z.append(w)
	text = tuple(z)
print(text)


x=[]
for w in items_1:
	s = w["name"]
	x.append(s)
	tuplee= tuple(x)
print(tuplee)

print ("\n")



