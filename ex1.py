age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")

print (age, type(age))

try:
    sum = int(age) + int(height) + int(weight)
    print(sum)

except ValueError :
    print("this is very imp line")

