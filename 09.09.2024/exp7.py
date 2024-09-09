def factorial(n):
    if n==0 or n==1:
        return 1
    elif n < 0:
        return -1
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    print(factorial(5))
    print(factorial(-12))
    print(factorial(0))