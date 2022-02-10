#defining a function to find repeated items in a tuple
def repeatedItems(t):

    #initializing an empty list 
    l=[]

    #inserting the repeated items into the empty list
    for i in range(len(t)):
        if t.count(t[i])>1:
            l.append(t[i])
    
    #typecasting the list into a set to avoid repeated number of repeated items
    l=set(l)

    return f"\nRepeated item in the tuple {t} is \n{l}.\n"

#creating a tuple
t=(1,1,2,2,3,3,3,4)

#function call
z=repeatedItems(t)

print(z)