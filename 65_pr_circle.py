from cmath import pi

#defining a class circle
class circle:

    #defining its attributes
    def __init__(self,radius) :
        self.radius=radius

    #defining a function to show the area
    def showarea(self):
        return f"\nThe area of the circle of radius {self.radius} is {pi*(self.radius**2)}"

    #defining a function to show the perimeter
    showperimeter= lambda self: f"\nThe perimeter of the circle of radius {self.radius} is {2*pi*self.radius}.\n"
try:
    #enters the radius of the circle from the user
    r=eval(input("\nEnter the radius of the circle : "))

    #function calling
    c=circle(r)
    print(c.showarea())
    print(c.showperimeter())

except Exception as e:
    print(f"\nInvalid Input!\n{e}\nPlease enter a numeric input and try again.\n ")