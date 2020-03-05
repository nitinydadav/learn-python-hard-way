dps = {"rohan":1001 ,"sohan":1002, "mohan":1003, "bil":1006, "kill":1005, "jon":1007, "kim":1008}
print dps 


for school,code in dps.items():
    print (school,"name and ID is",code) 
print "\n"

for y,z in enumerate (["jak", "jon", "sam", "janny"]):   # the position index and corresponding value 
    print (y,"index or name", z)
  
print "\n"

q = ["name", " hair color", "class"]
w = [ "jon", "black", "four"]

for x, a in zip(q, w):                                    # sequences at the same time
    print ("what is your {0}? here is  {1}.".format (x, a))

print "\n"

for a in reversed(range(1,10,4,)): # forward direction and then call the reversed() function.
    print (a)    
print "\n"
for r in reversed(range(1,20,2)):
    print (r)

print "\n"

cat = ["apple", "cat", "egg", "fish", "dog", "boll"]   #sequence in sorted order

for c in sorted(set(cat)):
    print (c)

met = [1,3,5,2,4,7,6,8,9]

for v in sorted(set(met)): 
    print (v)

print "\n"

import math
data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8] 
filtered =[]
for b in data:
    if not math.isnan(b):
     filtered.append (b)

print filtered


