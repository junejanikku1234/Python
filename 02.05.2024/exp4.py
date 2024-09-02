def checkPrime(n):
    if (n<=1):
        return False
    i = 2
    while (i<=n-1):
        if (n%i==0):
            return False
        i += 1
    return True

def checkArmstrong(n):
    str_Num = str(n)
    sum = 0
    int_len = len(str_Num)
    for i in str_Num:
        sum += int(i)**int_len
    return sum == n

if __name__ == "__main__":
    print(checkPrime(10))
    print(checkArmstrong(153))