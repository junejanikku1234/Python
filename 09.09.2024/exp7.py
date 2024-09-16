def factorial(n):
    if n==0 or n==1:
        return 1
    elif n < 0:
        return -1
    else:
        return n * factorial(n-1)

def my_function(a, b, c=10, d=20):
    print(a, b, c, d)

if __name__ == '__main__':
    print(factorial(5))
    print(factorial(-12))
    print(factorial(0))

    my_function(1, 2)
    my_function(1, 2, 3)
    my_function(1, 2, 3, 4)
    my_function(d=20, c=10, a=1, b=2)