

class SquareRoot(object):
    def __init__(self, a):
        self.a = a

    def sqrt(self):
        return self.a**0.5


class Addition:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.b+self.a


class Subtraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def subtract(self):
        return self.a-self.b


class Multiplication:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def multiply(self):
        return self.a*self.b


class Division:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def divide(self):
        return self.a/self.b


class MathNew(SquareRoot, Multiplication, Addition, Division, Subtraction):
    def __init__(self, a, b):
        self.a=a
        self.b=b
        super().__init__(a)


ob = MathNew(3,4)
print(ob.add())
print(ob.multiply())
print(ob.divide())
print(ob.sqrt())
print(ob.subtract())
