# def reverse1(s):
#     if len(s)==1 :
#         return s[len(s)-1]
#     else:

#         return s[len(s)-1]+reverse(s[0:len(s)-1])

#defining a function
reverse= lambda s: s[len(s)-1] if len(s)==1 else s[len(s)-1]+reverse(s[0:len(s)-1])

#inputs a string from the user
s=input("\nEnter a string : ")

#function calling
r=reverse(s)
print(f"\nThe reverse of the string '{s}' is : \n{r}.\n")