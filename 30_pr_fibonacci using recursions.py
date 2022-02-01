#defining a function fibonacci
def fibonacci(n):
    #storing the value of the first and second values of fibonacci series
    if n==0 or n==1:
        return n
    #using recursion
    else:
        return fibonacci(n-1) + fibonacci(n-2)

try:
    #inputs a number from the user
    n=int(input("\nEnter any non-negative number : "))

    #making sure that the inputted number is not negative
    while n<0:
        n=int(input(f"\n{n} is a negative number.\nPlease enter any non-negative integer : "))

    #calling the function
    f=fibonacci(n)

    #printing the result
    print(f"\nThe required fibonacci number is \n{f}.\n")
    
except:
    print('\nInvalid input.\nPlease enter a numeric value.\n')