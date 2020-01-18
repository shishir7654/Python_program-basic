class Calculation1:
    def sum(self,a,b):
        return a+b;

class Calculation2:
    def mul(self, a,b):
        return a*b;

class Derived(Calculation1,Calculation2):
    def div(self,a,b):
        return a/b;

d = Derived()

print(d.sum(10,20))
print(d.mul(10,20))
print(d.div(10,20))
