#defining a function which return the tuple containing the digits of the given number
def sumofdigits(x):
    
    #creating a list 
    l=[]
    if x>=0:
        x=str(x)

    else:
        x=str(-x)
    #appending the digits of the number in the list
    for i in range(len(x)):
        l.append(int(x[i]))

    #returning the values as a tuple
    return tuple(l)

try:
    #inputs an integer from the user
    x=int(input("\nEnter any number : "))

    #function calling
    sum=sum(sumofdigits(x))
    print(f"\nThe sum of the digits of the number {x} is :\n{sum}.\n")

except:
    print("\nInvalid input!Please enter a numeric integer value : ")