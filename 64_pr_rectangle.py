#defining a class rectangle
class rectangle:

    #defining the attributes of the class
    def __init__(self,length ,breadth):
        self.length=length
        self.breadth=breadth

    #defining a function to show the area    
    def showarea(self):
        return f"\nThe area of the reactangle is {self.length*self.breadth}.\n "
    
    #defining a function to show the perimeter
    def showperimeter(self):
        return f"\nThe perimeter of the rectangle is {2*(self.length+self.breadth)}.\n"

try:
    #inputs the length and breadth from the user
    l=eval(input("\nEnter the length of the rectangle : "))
    b=eval(input("\nEnter the breadth of the rectangle : "))

    #function call
    r=rectangle(l,b)
    print(r.showarea())
    print(r.showperimeter())

except Exception as e:
    print(f"\nInvalid Input!\n{e}\nPlease enter a numeric input and try again.\n ")