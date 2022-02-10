import re


count=lambda w: len(re.findall(r"\w+", w))
w=input ("\nEnter a sentence : ")
print(f"\nThe number of words present in the above sentence is {count(w)}.\n")