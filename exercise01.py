# learn-python-hard-way

string_1 = "learn"
string_2 = "python"
string_3 = "for"
string_4 = "fun and profit"

string_5 = string_1 + string_2 + string_3 + string_4
print(string_5)

# calulate the length of string_5 
print(len(string_5))

#  reverse string  
#output=str[-1]+str[-2]+str[-3]+str[-4]+str[-5]
#print(output)

reverse = "" .join(reversed(string_5))
print(reverse)
