
try:
    a,b = map(int,input("Hello! please enter two numbers for division seperated by a space: ").split())
    print(a/b)
    t = int(input("enter 1 if you want to increment the number:"))
    if(t==1):
        x = input("enter the number by which result should be incemented:")
    print(a / b + int(x))

except NameError:
    print("so you don't want the number to increment.")
except ArithmeticError:
    print("don't divide by zero")
except KeyboardInterrupt:
    print("you have entered wrong inputs")
finally:
    print('You are exiting out of program')
    exit(0)

