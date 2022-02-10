#defining a function which return the tuple containing the digits of the given number
def factors(x):
    
    #creating a list 
    l=[]
    
    if x<0:
        x=(-x)
    #appending the factors of the number in the list
    for i in range(1,x):
        if x%i==0:
            l.append(i)

    #returning the values as a tuple
    return tuple(l)

try:
    #inputs an integer from the user
    x=int(input("\nEnter any number : "))

    #function calling
    if x==sum(factors(x)):
        print(f"\nThe number {x} is a perfect number.\n")
    else:
        print(f"\nThe number {x} is not a perfect number.\n")
        
except:
    print("\nInvalid input!Please enter a numeric integer value : ")