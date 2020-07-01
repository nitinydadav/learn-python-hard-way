
#Given an integer,n , perform the following conditional actions:
# If n is odd, print Weird
#If n is even and in the inclusive range of 2 to 5,print Not Weird
#If n is even and in the inclusive range of 6 to20 , print Weird
#If n is even and greater than 20, print Not Weird
#

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

