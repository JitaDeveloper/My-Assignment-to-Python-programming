def nCr(n,r):

    r_f=1
    for i in range(1,r+1):
        r_f*=i


    c=1
    for i in range(n,n-r,-1):
        c*=i
    return f"\n{n}C{r} = {int(c/r_f)}\n"

print("\nWe will find the value of nCr!\n")
try:    
    n=int(input("Enter the value of n : "))
    while n<=0:
        n=int(input(f"\n{n} is a non-positive number.\nPlease enter a positive integer here : "))
    r=int(input("Enter the value of r : "))
    while r<=0:
        r=int(input(f"\n{r} is a non-positive number.\nPlease enter a positive integer here : "))
    C=nCr(n,r)
    print(C)
except:
    print("\nInvalid input!\nPlease enter a numeric value.\nYou must enter a positive integer only to get the required result.\n\nThank you.\n")

