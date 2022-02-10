#defining a function for shifting a character
def charShift(str):
    #defining a variable for storing the new string after shifting
    new_word=""

    #using a loop for shifting the characters by two place ahead
    for i in range (len(str)):
       
        ch=str[i]
        alpha="abcdefghijklmnopqrstuvwxyzab"
        ALPHA=alpha.upper()
        if ch in alpha:
            j=alpha.find(ch)
            j+=2
            ch=alpha[j]
            new_word+=ch
        elif ch in ALPHA:
            j=ALPHA.find(ch)
            j+=2
            ch=ALPHA[j]
            new_word+=ch
        else:
            new_word+=ch

    return f"\nThe new string after shifting the characters by two place ahead of it is : \n{new_word}\n"

str=input("Enter a string : ")
c=charShift(str)
print(c)
