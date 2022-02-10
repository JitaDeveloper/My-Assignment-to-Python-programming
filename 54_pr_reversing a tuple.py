#defining a function reverse
def reverse(t):
    
    #creating an empty list
    e=[]
    if len(t)==0 or len(t)==1:
        return f"\nThe reverse of the tuple {t} is : \n{tuple(t)}\n"
    else:
        # reversing a list
       for i in range(len(t)):
           e.append(t[len(t)-i-1])
       return f"\nThe reverse of the tuple {t} is : \n{tuple(e)}\n"

# creating a tuple
t=(1,3,"Jit",4,5,7)
# t=(2,)


#function call
z=reverse(t)
print (z)