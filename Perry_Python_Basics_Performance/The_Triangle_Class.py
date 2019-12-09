"""
25/25 points. 

Great job on error handling invalid triangles. 
"""

#Math is imported for calculating area of triangle
import math

#Class name is Triangle
class Triangle:
    def __init__(self,color,side1 = 1.0,side2 = 1.0,side3 = 1.0,filled = True):
        self.__color = color
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3
        self.__filled = filled

    #Setter for color
    def set_color(self,color):
        self.__color = color

    #Setter for side1
    def set_side1(self,side1):
        self.__side1 = side1

    #Setter for side2
    def set_side2(self,side2):
        self.__side2 = side2

    # Setter for side3
    def set_side3(self,side3):
        self.__side3 = side3

    # Setter for filled
    def set_filled(self,filled):
        self.__filled = filled

    # Setter for color
    def get_color(self):
        return self.__color

    # Getter for side1
    def get_side1(self):
        return self.__side1

    # Getter for side2
    def get_side2(self):
        return self.__side2

    # Getter for side3
    def get_side3(self):
        return self.__side3

    # Getter for filled
    def isFilled(self):
        return self.__filled

    # Getter for area
    def getArea(self):
        #s represents size of which is a critical component for Heron's formula
        s = (self.__side1 + self.__side2 + self.__side3) / 2
        area = math.sqrt(s * (s - self.__side1) * (s - self.__side2) * (s - self.__side3))
        return f'{area:.4f}'

    # Getter for Perimeter
    def getPerimeter(self):
        return self.__side1+self.__side2+self.__side3

    # Getter for __str__
    def __str__(self):
        print("Triangle definition: A plane figure with three straight sides and three angles")


#Main function
def main():
    create_triangle()

#Function for user input, create triaingle, and show data
def create_triangle():
    color = input("Enter color of your triangle: ")
    #Using function to validate triangle
    triangle = triangle_validate()
    filled = input("Would you like your triangle filled? ('y' for yes):")
    if filled.lower() == 'y':
        filled = True
    else:
        filled = False
    #Initialize triangle
    triangle = Triangle(color,triangle[0],triangle[1],triangle[2],filled)
    print(f'Area: {triangle.getArea()}')
    print(f'Perimeter: {triangle.getPerimeter()}')
    print(f'Color: {triangle.get_color()}')
    print(f'Filled: {triangle.isFilled()}')

#This functions verifies the validity of the triangle
def triangle_validate():
    triangle = False
    #Empty place holders for each side of the triangle
    a = ''
    b = ''
    c = ''
    while triangle == False:
        a = input("Enter the size of side 1 of your triangle: ")
        a = input_validation(a)
        b = input("Enter the size of side 2 of your triangle: ")
        b = input_validation(b)
        c = input("Enter the size of side 3 of your triangle: ")
        c = input_validation(c)
        if (a + b > c) and (a + c > b) and (b + c > a) :
            triangle = True
        else:
            print("INVALID TRIANGLE! Try again:")
            triangle = False
    return [a,b,c]

#Simple input validation
def input_validation(num):
    is_float = False
    while is_float == False:
        try:
            float(num)
            is_float = True
        except:
            num = input(f'{num} is not a number. Please enter a number in place of {num}: ')
            is_float = False
    return float(num)

main()




