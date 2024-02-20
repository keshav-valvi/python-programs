# KESHAV VALVI
# FY23N052

# Program to calculate area of polygons

def calculate_area(name):
    # convert all the characters into lowercase
    name = name.lower()
    
    # check for the condition
    if name == "rectangle":
        l = int(input("Enter the length of rectangle: "))
        b = int(input("Enter the breadth of rectangle: "))
        # calculate the area of rectangle
        rect_area = l * b
        print(f"The area of rectangle is {rect_area}.")
    elif name == "square":
        s = int(input("Enter the side of the square: "))
        # calculating the area of the square
        sqr_area = s * s
        print(f"The area of square is {sqr_area}.")
    elif name == "triangle":
        h = int(input("Enter the height of triangle: "))
        l = int(input("Enter the length of triangle: "))
        # calculating area of triangle
        tri_area = 0.5 * h * l
        print(f"The area of triangle is {tri_area}.")
    elif name == "circle":
        pi = 3.14
        r = int(input("Enter the radius of circle: "))
        # calculating area of circle
        circ_area = pi * r * r
        print(f"The area of circle is {circ_area}.")
    else:
        print("Sorry, this shape is not available.")

# Driver code
if _name_ == "_main_":
    print("Calculate shape area:")
    shape_name = input("Enter the name of shape: ")
    # function calling
    calculate_area(shape_name)