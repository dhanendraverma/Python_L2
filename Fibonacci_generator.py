a = int(input('Enter the no of terms to be printed: '))

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

b = fib()
b.__next__()

for i in range(a):
    print(b.__next__())