#defining a function which checks a number is prime or not
def prime(n):
    if n==1 or n==2 or n==0:
        return 1

    else:
        p=True
        for i in range(2,n):
            if n%i==0:
                p=False
                break
        if p:
            return 1
        else:
            return 0

#defining a function fibonacci
def fibonacci(n):
    #storing the value of the first and second values of fibonacci series
    if n==0 or n==1:
        return n
    #using recursion
    else:
        return fibonacci(n-1) + fibonacci(n-2)


try:
    a=int(input("\nEnter a positive integer : "))

    print(f"\nAll the prime Fibonacci numbers upto {a} are : \n")
    for i in range(a+1):
        if fibonacci(i)<=a:
            if prime(fibonacci(i))==1:
                print (fibonacci(i),end=",")
        

    print("\n")

except:
    print("\nInvalid input!\nPlease enter a numeric value.\n")
