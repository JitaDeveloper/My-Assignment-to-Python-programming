'''defines a function for addition'''
def addition(n1,n2):
    # adds two given numbers
    a=n1+n2

    # returns the Value
    return f"\nThe addition of the numbers {n1} and {n2} is {a}.\n"

''' defines a function for substraction'''
def substraction(n1,n2):
    # substracts the given numbers
    s=n1-n2

    # returns the result
    return f"\nThe substraction of the number {n2} from {n1} is {s}.\n"

'''defines a function for multiplication'''
def multiplication(n1,n2):

    # multiplies the given numbers
    m=n1*n2

    # returns the result
    return f"\nThe multiplication of the numbers {n1} and {n2} is {m}.\n"

''' defines a function for division'''
def division(n1,n2):
    #the divisor must be not equal to zero
    if n2!=0:
        
        #divides the numbers if the divisor is not equal to zero
        d=n1/n2
        d=f"\nThe division of the numbers {n1} and {n2} is {d}.\n"

    else:
        #returns "Math Error!" if the divisor is zero.
        d="Math Error!"
    
    # returns the result
    return d

''' defines a function for modulus'''
def modulus(n):
    #checks if the given number is positive or negative or zero
    #then finds the absolute value of the given number
    if n>=0:
        m=n
    else:
        m=-n

    # returns the result
    return f"\nThe modulus of the number {n} is {m}.\n"

''' defines a function for exponent'''
def exponent(n1,n2):
    #performs the operation for getting exponents
    e=n1**n2

    # returns the result
    return f"\nThe exponent of the number {n1} to {n2} is {e}.\n"
try:
    print(addition(2,3))
    print(substraction(2,3))
    print(multiplication(2,3))
    print(division(2,3))
    print(modulus(-9))
    print(exponent(2,3))

except:
    # handling the program from invalid inputs from the user
    print("\nPlease enter a numeric input.\n")

