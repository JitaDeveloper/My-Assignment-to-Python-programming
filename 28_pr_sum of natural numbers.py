#defining a function sum to get the sum
def sum(n):
    #if n=1 it will return 1
    if n==1:
        return 1

    #using recursion
    else:
        return n + sum(n-1)

try:
    #input a number from the user
    n=int(input("\nEnter any natural number : "))

    #making sure that n is a natural number
    while n<=0:
         n=int(input(f"\n{n} is not a natural number.\nPlease enter a natural number here : "))

    #calling the function
    s=sum(n)

    #printing the result

    print(f"\nThe sum of the first {n} natural numbers is \n{s}.\n")
    
except:
    print("\nInvalid input!\nPlease enter a numeric input.")  