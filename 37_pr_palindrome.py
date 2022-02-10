#inputs a string from the user
n=input("\nEnter any string here: ")

#initializing a variable to store the reversed string
rev_n=""

#initializing a loop for finding the reversed string
for i in range(len(n)):
    rev_n+=n[len(n)-1-i]

#checking the condition for being palindrome
if n==rev_n:
    print (f"\n'{n}' is a palindromic string.\n ")
else:
    print(f"\n'{n}' is not a palindromic string.\n")