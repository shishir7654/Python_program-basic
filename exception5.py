class Networkerror(RuntimeError):
    def ___init__(self,arg):
        self.arg = arg

try:
    raise Networkerror("Error")

except Networkerror as e:
    print(e.args)
