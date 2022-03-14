try:
  def check_prime(n):
    if n > 1:
      res = True
    for i in range(2, n):
        if n % i == 0:
          res = False
          break
   return res
def prime(n):
if not check_prime(n):
factors = []
for i in range(2, n):
if n % i == 0 and check_prime(i):
factors.append(i)
elif check_prime(n):
factors = [1]
else:
factors = [0]
return factors
n = int(input('Enter a number: '))
print(str(prime(n))[1:-1])
except:
# handling the program from the invalid inputs by the user
print("\nInvalid input!\nPlease enter a valid integer.\n")
