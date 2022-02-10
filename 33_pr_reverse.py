#inputs a string from the user
n=input("\nEnter any string here: ")

#initializing a variable to store the reversed string
rev_n=""

#initializing a loop for finding the reversed string
for i in range(len(n)):
    rev_n+=n[len(n)-1-i]
print (f"The reverse of the string '{n}' is \n'{rev_n}'")
