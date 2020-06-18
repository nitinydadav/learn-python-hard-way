def get_key (val):
    for key , value in a.items():
        if val == value :
            return(key)
    return("key this is not in the dict ")

a = {"a":1,"b":2,"c":"","d":4,"e":""}

print(get_key(""))
print(get_key(""))
print(get_key(a))
