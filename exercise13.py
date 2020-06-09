#Parameters, Unpacking, Variables

from sys import argv
script,first,second,third = argv
print("argv: ",)
print("argv: type", type(argv))
print("argv:0 ", argv[0])
print("argv:1 ", argv[1])
print("argv:2 ", argv[2])
print("argv:3 ", argv[3])
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third )


# output 
"""
The script is called: ex13.py
Your first variable is: first
Your second variable is: 2nd
Your third variable is: 3rd
"""
