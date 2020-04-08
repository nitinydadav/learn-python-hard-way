# Class Method with parameter
  #   self ---- self is a variable which refer to current class object .
class calc:
    def add(self,x,y):
        self.answer = x + y
        print(self.answer)
        print(type(self.answer))

    def sub(self,x,y):
        self.answer = x - y
        print(self.answer)

    def mult(self,x,y):
        self.answer = x * y
        print(self.answer)

    def div(self,x,y):
        self.answer = x / y
        print(self.answer)
moon = calc()
print(moon.add(5, 7))
print(moon.sub(5, 7))
print(moon.mult(5, 7))
print(moon.div(5, 7))
print(id(moon))
