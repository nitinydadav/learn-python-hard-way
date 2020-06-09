
## step1
print("hello: 1")

## step2
hello = "hello: 2"
print(hello)


"""
define funtion without parmeter/return
"""
def print_hello():
	print(hello)

print(print_hello())



def print_hello():
	hello = "hello:3"
	hello_2 = "heloo this"
	print(hello +"__"+ hello_2)

print(print_hello())


"""
define funtion with return
"""
def print_hello():
	hello =  "hello:4"
	return hello


ret_val = print_hello()
print(ret_val)



"""
define function with parameter
"""
def hello_world(aa, bb, cc):
	pass

hello_world("mao", "mao", "cat")



def hello_world(a):
	print(a + "world"+hello)

hello_world("mao mao ")


import threading     # Main thread creating python virtual machine (pvm).
t = threading.current_thread().getName()
print("Nitin yadav")
print(t)

print("\n")

from threading import Thread

def disp(a,b):
		print("child thread", a , b)

y = Thread( target = disp , args = (10,20) )
print(y.start())

for i in range(5):
	print("main thread")


def Fun(*argv):
	if len(argv) == 3:
		print ("hello your name is",argv[0],"and your age is",argv[1],"phone nub is",argv[2])
	else:
		print ("hello your name is", argv[0],"and your age", argv[1])
lst = ("Bosko", 3, 7982902258)
print (Fun(*lst))




def prt(** bo):
	for key,value in bo.items():
		print (key,value)
mark =  {"bosko":2020, "bok":201,"tok":420, "abc":123}


print(prt(**mark))

print("\n")
def marks(mad,*arg ,**argv):
	print ("hello would",mad)
	for i in arg :
		print ("hello this is the",i)
		print(type(i))
	for k,v in argv.items():
		print (k,v)

lst = [8, 5]

dit = {"boskoo":202, "bokkk":200,"tokkkk":4200, "abcccc":1123,}

print (marks("nitin", *lst, **dit))

print("\n")


def drop(a , b):
	while a<=b:
		yield a
		a+=1

q = drop(1, 5)
print (q)
print (type(q))

print(next (q))
print(next (q))
print(next (q))
print (next(q))
print (next(q))


a = input("jojo ")
b = input ("gooo ")
print( " you are %r in is are %r:" %(a,b ))