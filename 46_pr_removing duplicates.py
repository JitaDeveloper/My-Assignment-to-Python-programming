#creating a list
l=[1,1,1,33,5,5,99]

#removing the duplicate by converting the list into a set
s=set(l)

#further converting the set to a list
l1=list(s)

#printing the final list
print (f"\nThe final list after removing all the duplicates from list {l} is :\n {l1}\n")