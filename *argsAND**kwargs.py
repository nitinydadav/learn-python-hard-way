# *args make tuple
# ** kwargs make dictionary

def waah(*args,**kwargs):
    print (type(args),args)
    print (type(kwargs),kwargs)
print(waah(10,20, k=10))


def waao(a,b,**sodo):
    print (a,b)
    print (type(a))
    print (sodo)
    print (type(sodo))

print(waao(10,20,k=40))




