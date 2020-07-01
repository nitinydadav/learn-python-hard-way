
class Sum:
    def Add(cls,r):
        cls.ram = r
        return("RRRAM",cls.ram)
roof = Sum()
print(roof.Add("20gb"))
