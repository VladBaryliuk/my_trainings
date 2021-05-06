factorial = 1

def factorial_of_something(dig):
    global factorial
    for i in range(1,dig+1):
        factorial *= i

factorial_of_something(20)
print(factorial)
