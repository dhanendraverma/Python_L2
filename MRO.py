

class First():
    def method1(self):
        print("Class First's method1")


class Second(First):
    def method1(self):
        print("Class Second's method1")


class Third(First):
    def method1(self):
        print("Class Third's method1")


class Fourth(Second, Third):
    def method1(self):
        print("Class Fourth's method1")

print("MRO from Fourth class is",Fourth.__mro__)
