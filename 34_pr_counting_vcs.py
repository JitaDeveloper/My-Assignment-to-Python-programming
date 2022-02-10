
#defining a function for counting
def count(sen):
  
    #defining variables for storing the result
    vowels = 0
    consonant = 0
    specialChar = 0
    space = 0

    #using a loop for finding out the number of vowels, consonants, spaces and special characters
    for i in range(0,len(sen)):
        l=sen[i]

        #condition for counting alphabetical strings i.e., vowels and consonants
        if (l>="a" and l<="z") or (l>="A" and l<="Z"):
            l=l.upper()
            v=["A","E","I","O","U"]
            if l in v:
                vowels+=1
            else:
                consonant+=1

        #conditions for counting space
        elif (l==" "):
            space+=1
        
        #code for neglecting the numeric characters
        elif(l>="0"and l<="9"):
            pass

        #code for counting the special characters
        else:
            specialChar+=1
    
    return f"\nThe number of vowels present  is : {vowels} \nThe number of consonants present is : {consonant}.\nThe number of spaces present is : {space}.\nThe number of special characters present is : {specialChar}.\n"

#inputs a sentence from the user
sen=input("\nEnter a sentence : ")

#function call
c=count(sen)
print(c)





