# Asking Questions

x = input("what's your name? ")
age = input("how old are you? ")
city = input("where are you living? ")
stdy = input("Are you graduate? ")
cont = input("which country you want to go? ")
vsa = input ("have you apply vsa? ")
mny = input("how much money do have? ")

print ("Hello, %r , You are %r old, you'r %r location is, you'r %r, your country %r is right, you have vsa %r that's good and %r mony book your ticket your self." % (x,age,city,stdy,cont,vsa,mny,))







import exercise12
flag = 0
q = input(">enter the name ")
w = input("file name   ")
try:
    opening = open (w,"rr")
except:
    print("no file found ")
    quit()

for word in opening:
    eng_word = word.encode("utf-8")
    digest = exercise12.the(eng_word.strip()).hexdigest()
    if digest == q :
        print("password found")
        print("password is " + word )
        flag = 1
        break
if flag == 0:
    print("password not found is not in the list ")




#https://www.youtube.com/watch?v=CV_mMAYzTxw&list=WL&index=3&t=425s