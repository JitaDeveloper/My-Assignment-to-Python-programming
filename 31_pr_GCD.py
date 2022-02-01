# defining a function to get GCD
def GCD(n1,n2):
    if n2==0:
        return n1
    #using recursions
    else:
        return GCD(n2,n1%n2)

try:
    #input two numbers from the user
    n1=int(input("\nEnter the first natural number : "))
    #making sure that the inputted numbers are not negative
    while n1<=0:
        n1=int(input(f"\n{n1} is a negative number.\nPlease enter any natural number : "))

    n2=int(input("\nEnter the second natural number : "))
    while n2<=0:
        n2=int(input(f"\n{n2} is a negative number.\nPlease enter any natural number : "))

    #calling the function
    f= GCD(n1,n2)

    #printing the result
    print(f"\nThe Greatest Common Divisor of the numbers {n1} & {n2} is : {f}.\n")
    
except:
    print('\nInvalid input.\nPlease enter a numeric value.\n')