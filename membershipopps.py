# use of in =  its return true when element found otherwise  false
# not in  ,,, its returns true if element not found ,,, and element is found then it return false.
def pub(pera):
    list = input("enter any number ")
    list1 = list in pera
    list2 = list not in pera
    return ("your number is ", list , "operator in is", list1, "not in is ", list2)
w = range(70)
print(pub(w))

