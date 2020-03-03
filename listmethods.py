a = [1, 2, 3, 4, 5, 2, 2]

print a 

print a[0]
print a[4]
print a[-1]
print a[-7]
print a[:]
# list support operations like concatenation
print a + [22, 33, 44, 55, 66]


b = [11, 22, 33, 44, 22]
print b
print 6**2

b[2] = 36
print b

print len(a)    # total value of a 

word = ["hello", "world", "python", "github", "nit"]
print word

word[1:3] = []
print word

word[:] = []

print word 

c = [1, 2, 3, 4]
d = ['a', 'b', 'c', 'd', 'e']
e =[c, d]
print e

print e[0]
print e[0][1]

print '\n'
print d
print '\n'

print len(d)

egg = ["A", "b", "c", "d" , "e"] 
print egg
egg.append("F")	      #  add  elements
print egg 

egg.append("b")
print egg
print "\n"																															
print egg.count("b")
print egg.count("c") 
print "\n"

add =  [1, 2, 3, 4,]
some = ["a", "b", "c", "d"]
print add 
print some 	
add.extend(some)
print add
 


print egg.index("A")

print egg.index("d")
print add
add.insert(5, 'a')
print add

 
add.insert(1, '2')

print add



add.pop()       # last content will be  removed 
print add
 

add.pop(6)      # sixth element will be removed this will not retun

print add  	


add.remove(1)
print add

add.remove("c")
print add


def reverse(add):
    return [ele for ele in reversed (add)]
print (reverse(add)) 



add.sort()

print add
