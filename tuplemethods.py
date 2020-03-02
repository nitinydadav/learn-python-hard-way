n = 123, 321, 123, 333, 333, 123,
print n 

print n.count(123)
print "\n"

print n.count(321)
print "\n"

print n.count(333)



# uses of index 

y = ('boski','nav', 'yad', 'boski')
print "\n"

print y

print "\n"

print y.index("boski")

print "\n"

print y.index('yad')
print y.index("abc")

"""
ValueError                                Traceback (most recent call last)
<ipython-input-83-6eedd2b68194> in <module>()
----> 1 n.index(666)

ValueError: tuple.index(x): x not in tuple
"""
