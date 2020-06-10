#Given an integer, n, perform the following conditional actions:
#If n is odd, print Weird
#If n is even and in the inclusive range of 2 to 5, print Not Weird
#If  is even and in the inclusive range of 6 to 20, print Weird
#If  is even and greater than 20, print Not Weird


item = int(input("enter the num "))
if item%2 == 1 :
    print("Odd   weird ")
if item%2 == 1 and 2<= item<=5:
    print("lessthen 2 & 5 not weird")
elif item%2 == 1 and 6<= item<=20:
    print("under the 6 or 20 weird")
elif  item >= 20 :
    print("this is greter then 20  ")
else:
    ("this is the else part ")
