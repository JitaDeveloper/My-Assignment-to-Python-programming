#inputs two numbers from the user
a=eval(input("\nEnter the first number : "))
b=eval(input("Enter the second number : "))

#printing the results before swapping
print(f"\nBefore swapping first number = {a} & second number = {b}.")

#swapping the numbers
a,b=b,a

#printing the final results after swapping
print(f"\nAfter swapping first number = {a} & second number = {b}.\n")
