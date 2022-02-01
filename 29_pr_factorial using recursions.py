#defining a function for getting the factorial
def factorial(n):
    #adjusting the values for 1! & 0!
    if n==0 or n==1:
        return 1
    #using recursive functions
    else:
        return n*factorial(n-1)

try:
    #inputs a number from the user
    n=int(input("\nEnter any non-negative number : "))

    #making sure that the inputted number is not negative
    while n<0:
        n=int(input(f"\n{n} is a negative number.\nPlease enter any non-negative integer : "))

    #calling the function
    f=factorial(n)

    #printing the result
    print(f"\nThe factorial of {n} is equal to \n{f}.\n")
    
except:
    print('\nInvalid input.\nPlease enter a numeric value.\n')