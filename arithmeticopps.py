# use oprent

a = 10
b = 20
c = a + b
print(c)
print(type(c))

print("\n")

q = a - b
print(q)

print("\n")

c = a * b
print (c)
print(type(c))

print ("\n")

c = b / a
print(c)
print(type(c))

print("\n")

a = 7
b = 4
x = a % b
print(x)
print(type(x))

print("\n")

x = a ** b
print(x)

print("\n")

x = a // b
print(x)

print("\n")

x = -a // b
print(x)

print ("\n")

def arithmetic_ops(x,y):
    a = x + y
    b = x - y
    c = x * y
    d = x / y
    e = x % y
    f = x ** y
    g = x // y
    return a,b,c,d,e,f,g
add, sub, multi, divi, modu, sqr, dobslash = arithmetic_ops(20 , 15)
print(add)
print(sub)
print(multi)
print(divi)
print(modu)
print(sqr)
print(dobslash)