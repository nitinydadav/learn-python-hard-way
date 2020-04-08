# static method with parameter

class stac:
    @staticmethod        #decorator
    def static(x,y):       # static method
        q = x+y
        return(q)
wwf = stac()
print(wwf.static(10,20))     # calling static  method



class Klas :
    q = 10
    def prnt(self):
        print(id(self))
        print("vodka",Klas.q)


xx = Klas()
print(id(xx))
print(xx.prnt())


