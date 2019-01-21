class TestIterator():
    def __init__(self,l):
        self.data = l
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.index -= 1
        if -(self.index) > len(self.data):
            raise StopIteration
        return self.data[self.index]


l = [2,5,3,5,5,6]
r = TestIterator(l)
itr = iter(r)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))