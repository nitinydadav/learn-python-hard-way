a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (type(n1+n2+n3))
print("N1",n1)
print("N2", n2)
print("N3",n3)
print("two ", n1+n3)
