# defining the function
def longintfact(n):
    try:
        #defining a variable factorial
        factorial=1
        
        # making sure that the given number is not a negative number
        while n<0:
            n=int(input(f"\n{n} is a negative number.\nPlease enter any positive integer : "))

        #creating a loop by which the factorial of the given number will be calculated
        for i in range(1,n+1):
            factorial*=i
        
        #writing the evaluated factorial of the given number in a statement
        factorial = f"\nThe factorial of the number {n} is {factorial}.\n"

    except:
        #handling the program from the invalid input by the user
        factorial="\nInvalid input!\nPlease enter a numeric value.\n"

    return factorial

f=longintfact(-1)
print(f)
