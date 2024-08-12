n = int(input("How many times do you want to check?: "))
for i in range(n):
    x = int(input(f"Enter the {i+1}th number to be checked: "))
    if(x>=0):
        print(f"{x} is positive.")
    else:
        print(f"{x} is negative.")
    if(x%2 ==0):
        print(f"{x} is even.")
    else:
        print(f"{x} is odd.")
