#List Comprehensions

#Let's learn about list comprehensions! You are given three integers X,Y and Z.epresenting the dimensions of a cuboid along with an integer N.
# You have to print a list of all possible coordinates given by (item,item1,item2) on a 3D grid where the sum of item+item1+item2is not equal to .
# Here,
x = int(input("x input "))
y = int(input("y input "))
z = int(input("z input "))
#n = int(input("n input "))
emt = []
p = 0
for item in range (x+1):
    for itrem1 in range(y+1):
        for item3 in range (z+1):
            if item + itrem1 + item3 != z:
                emt.append(item)
                emt.append(itrem1)
print(emt, end="")
