from sys import argv

script,filename = argv

print("we 're going to make a txt file %r." % (filename))
print("I don't want to hit ctrl-c (^c) in this file.")
print("I want to see my script, prees enter.")

input ("?")

print("opening my file ...")
target = open (filename, 'w')
print(type(target))
print("Now tauncating the file. Is not a Goodbye!")
target.truncate()

print("Now i want to tell you somthing.")

line1 = input ("should i lie down")
line2 = input ("stand up...")
line3 = input ("walk around")
line4 = input ("Aagin")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
target.write(line4)
target.write("\n")

print(" bye bye see you soon.")
target.close()
  
