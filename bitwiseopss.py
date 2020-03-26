# bitwise operator will get into binary result and then convert into decimal

item = 10
item1 = 14

# bitwise and &
print(item & item1)
print("\n")
#bitwise or |
print(item | item1)

print("\n")

#bitwise xOR ^
print(item^item1)

print("\n")

#bitwise not ~
print(~ item1)

print("\n")

#bitwise left shift <<

print("\n")

print(item << item1)
#bitwise right shift >>

print("\n")

print(item>>item1)



def bitwise(y,z):
    a = y & z
    b = y| z
    c = y ^ z
    d = y << z
    e = y >> z
    return a,b,c,d,e

And, Or,xor,leftshift , rightshift = bitwise(10,15)
print(And)
print(Or)
print(xor)
print(leftshift)
print(rightshift)
