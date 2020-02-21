from sys import argv

script, nitin  = argv
print argv
abc = open(nitin)

print "Here's your file %r:" % nitin
print abc.read()

print "Type the filename again:"
file_again = raw_input("> ")

abc_again = open(file_again)

print abc_again.read()
