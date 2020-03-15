for new in range(0,10):
	if new == 7:
		break
	print (new)

print("\n")

x = range(2, 20,2)
for new in x:
	if new ==16:
		break
	print(new)

print("\n")

lis = ["hello", "would", "it's", "time to", "wake up", "jon", "let's go to market"]
for news in lis:
	if news =="jon":
		continue
	print (news)


print ("\n")

lst = [1, 2,3,4,5,6]
for new in lst:
	if new % 2==1:
		continue
	print (new)

print ("\n")



def fung(my,lst):
	lst1 = []
	for new in my:
		if new in lst:
			continue
		lst1.append(new)
	return lst1

x = fung([1,2,3,4,5,6], [3,5])
print (x)
print ("\n")
def file(test,test1):
    new = []
    for doc in test:
        if doc in test1:
            break
        new.append(doc)
    return new
pub = file([1,2,3,4,5,6], [4])
print (pub)
