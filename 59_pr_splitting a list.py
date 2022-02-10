
def oddOrEven(l):
    l=l.split(",")
    lo=[]
    le=[]
    for i in range(len(l)):
        if int(l[i])%2==0:
            le.append(int(l[i]))

        else:
            lo.append(int(l[i]))
    return f"\nThe list of odd numbers are \n{lo}\n\n&\n\nThe list of even numbers is \n{le}\n"

l=input("\nYou have to enter the list in this format \na,b,c,d and so on.\nEnter a list : ")
print(oddOrEven(l))




