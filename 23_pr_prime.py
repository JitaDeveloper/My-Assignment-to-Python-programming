

def prime(n):
    sum=0
    count=0
    M=10**(n**n)
    for j in range(2,M+1):
        for i in range(2,j):
            if j%i==0:
            
                break
    
        else:
            sum+=j
            count+=1

        if count == n:
            break 

    return f"\nThe sum of the first {n} prime numbers is {sum}.\n"

n=int(input("Please enter a positive integer : "))
while n<=0:
    n=int(input("\nInvalid input!\nPlease enter a natural number here : "))
p=prime(n)
print(p)



    
