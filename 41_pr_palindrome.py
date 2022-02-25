import re
def palin(word):
    

    #initializing a variable to store the reversed string
    rev_n=""

    #initializing a loop for finding the reversed string
    for i in range(len(word)):
        rev_n+=word[len(word)-1-i]

    #checking the condition for being palindrome
    if word==rev_n:
       return 1
    else:
        return 0


def countPalindrome(sentence):
    #creates a list containing all the words in the sentence
    l=re.findall(r"\w+",sentence)
    count=0

    #finds the palindrome numbers and count them
    for i in range(len(l)):
        if palin(l[i])==1:
            count+=1
    
    return f"\nThe number of Palindromic words present in the given sentence is : {count} ."

#inputs a string from the user

sentence = input ("\nEnter any sentence here : ")

#function call
print(countPalindrome(sentence))
