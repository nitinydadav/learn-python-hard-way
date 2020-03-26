sav = {'jon': 4001, 
        'sam':4002,
        'kon':4003}

print (sav)

sav['jam'] = 5004

print (sav)

print (sav['sam'])

del sav['sam']
sav['kill'] = 4004

print (sav)

print (list(sav))  # it's return key used in dictionary


print (sorted(sav))

print ('jon' in sav )

print ('sam' in sav)

print ('kill' not in sav)

print (dict ([('jam', 5004), ('kill', 4004), ('jon', 4001), ('kon', 4003)])) # directly from sequences of key-value pairs


	

# let's add the value in dictonary 


sav['ston']=1233
print (sav)
	

# removeing key-value pairs with the < del > operator.

del sav['kon']
print (sav)

# len() function gives the number of pairs in the dictionary.

print (len(sav))

print (len('jam, jon'))

# pop remove element form the dictionary 	

sav.pop('jam')
print (sav)

# copy()

new = sav.copy()
print (new)

print ("\n")

print (sav)

print ("\n")

print ("\n")
 

print (new)

# update dictionary 

s ={'apple':8, 'banana':5.5, 'orenge':6}

sav.update(s)

print (sav)
print (s)


# find the key 

print (sav.keys())

#values 

print (sav.values())



