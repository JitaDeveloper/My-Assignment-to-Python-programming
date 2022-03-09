try: 
   # inputs a rental number from the user 
   n = eval(input("\nEnter rental number : ")) 
   if n>200: 
     bill = 100*0.2 + 100*0.3 + (n-200)*0.5 
   elif 100 < n <= 200: 
     bill = 100*0.2 + (n-100)*0.3 
   elif 0 < n <= 100: 
     bill = n*0.2 
   print(f'Telephone bill of Mr. X is Rs {bill}') 
except: 
 # handling the program from the invalid inputs by the user 
 print("\nInvalid input!\nPlease enter a valid rental number.\n")
