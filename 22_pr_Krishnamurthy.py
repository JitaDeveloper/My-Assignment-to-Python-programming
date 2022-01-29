


# defines a function for getting Krishnamurthy numbers
def Krishnamurthy(n):
    try:
        # defining a variable sum to store the value of the sum of the factorial of the  digits 
        sum=0

        #making sure that the value of the given number is not less than 0
        while n<=0:
            if n<0:
                n=int(input(f"\n{n} is a negative number.\nPlease enter a positive integer : "))
            elif n==0:
                n=int(input(f"\n0 is not a natural number.\nPlease enter a natural number : "))     
        #storing the value of the given number in a variable
        n1=n

        #starting a loop for getting the sum of the factorial of the digits
        while n>0:
            digit=n%10
            factorial=1
            for i in range(1,digit+1):
                factorial *=i 

            sum+=factorial
            n//=10

        #time for conclusion
        if sum==n1:
            print(f"\nThe number {n1} is a Krishnamurthy number.\n")
        else:
            print(f"\nThe number {n1} is not a Krishnamurthy number.\n")
    except:
        #handling the data from invalid inputs by the user
        print("\nInvalid input!\nPlease enter a numeric value.\n")

#inputs a number which we have to check
n=int(input("\nEnter any natural number : "))

#call of the function Krishnamurthy
Krishnamurthy(n)
        

