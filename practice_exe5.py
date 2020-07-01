#Write a function
   #Task
    #You are given the year, and you have to write a function to check if the year is leap or not.

     #Note that you have to complete the function and remaining code is given as template.

def leap(year):

    if year%4==0:
        return("Is True")
    elif year%100==0:
        return("False")
    elif year%400==0:
        return("True")
    else:
        return("False")

year = int(input("enter the year "))
print(leap(year))