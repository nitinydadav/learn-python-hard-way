
#a = input("Enter first num ")
#b = input("Enter second num ")

try:
    if int(a) > int(b):
        print(a + "  Is greater")
    else:
        print(b + " Is greater than  ")

except:
    print(" This is the error value ")

else:
    print("Two numbers compared successfuly ")


class mobile:
    @classmethod
    def cls(cls):
        print("vivo pro" )

xx = mobile
print(xx.cls())


class Sum:
    def Add(cls,r):
        cls.ram = r
        print("RRRAM",cls.ram)
roof = Sum()
print(roof.Add("20gb"))


#class funk:
 #   def add(cat,x,y):

#        cat.ans = x + y
 #       return(cat.ans)

#root = funk()
#print(root.add(10,20))
try:
    n = int(input("enter your lucky num > "))
    if n % 2  !=  0:
        print("weird")
    else:
        if n >= 2 and n <= 5:
            print("not weird ")
        elif n >= 6 and n <20:
            print("weird")
        elif n > 20:
            print("not weird" )
except:
    print ("you can not pass the string")


