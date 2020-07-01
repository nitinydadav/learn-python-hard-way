print ("""
Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are
       """)


#2
import sys
print("python version")
print(sys.version)
print("version info.")



from datetime import datetime
a = datetime.now()
print("this is the current date and time", a )



a = input ("enter 1 name ")
b = input("enter 2 name  ")

c = a + b
print(c)


l = input("fff ")
a = l.split(",")
x = tuple(a)
print(type(a),a)
print (type(x),x)


a = input("enter your name ")
c = a.split(",")
print(" this is :" + repr(c[-1]))


color_list = ["Red","Green","White" ,"Black"]
print("this the first  and last color :" , color_list[0],color_list[3])

exam_st_date = (11,12,2014)
print( "The examination will start from : %i / %i / %i"%exam_st_date)


a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (type(n1+n2+n3))
print("N1",n1)
print("N2", n2)
print("N3",n3)
print("two ", n1+n3)


import calendar
year = int(input("enter the year  "))
month = int(input("enter the the month "))
print(calendar.month(year,month))


print(""" 
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example

""")


a = int(input(" haaaa "))
b = 20
c = abs(a + b )
type(b)
print(c)

