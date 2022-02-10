import re
#defining a function for counting the number of words starting with 'S'


count_S=lambda s: len(re.findall(r"\bS\w+",s)) #using regex

#input any string from the user
s=input("\nEnter any sentence : ")

#function call
z=count_S(s)

#printing the result
print(f"\nThe number of words starting with 'S' in the above string is : \n{z}.\n")