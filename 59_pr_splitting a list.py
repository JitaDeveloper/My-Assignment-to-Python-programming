#defining a function to separate the odd and the even numbers
def oddOrEven(l):
    try:    
        #splitting the input to get the list
        l=l.split(",")

        #defining two variables to store the odd and even numbers respectively
        lo=[]
        le=[]

        #appending the odd & even numbers to the respective list
        for i in range(len(l)):
            if int(l[i])%2==0:
                le.append(int(l[i]))

            else:
                lo.append(int(l[i]))
        #returning the final results
        return f"\nThe list of odd numbers are \n{lo}\n\n&\n\nThe list of even numbers is \n{le}\n"


    except:
        return f"\nInvalid input! Please enter a numeric value.\n"

#inputting the number from the users
l=input("\nYou have to enter the list in this format \na,b,c,d and so on.\nEnter a list : ")
print(oddOrEven(l))




