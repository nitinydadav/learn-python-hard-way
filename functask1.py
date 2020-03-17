def colors():
    for key,val in x.items():
        print(key + ":" + val)


x = {"apple": "red", "orange": "orange", "egg": "white"}
print(colors())
print("\n")

def fun(q, w, e):
    q.update({w: e})
    return q


k='multiplex'
v='big-shop'

q ='colors'
w = ['red', 'organge', 'white']

new_x = fun(x, 'mkretail', 'shop')
print(new_x)
new_x = fun(new_x, k, v)
print(new_x)
new_x = fun(new_x, q,w)
print(new_x)


new_x = fun({"movie": "seven"}, "director", "david")
print(new_x)
