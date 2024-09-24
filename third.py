# Taking input of length and width of rectangle
length = float(input("Enter the length of the rectangle :"))
width = float(input("Enter the width of the rectangle :"))

# Calculating the area of the rectangle
area = length * width

# Printing the area of rectangle
print("The area of the rectangle is :", area)

# Using the format method to displays the area of rectangle with two decimal places
print("The area of the rectangle with two decimal: {:.2f}".format(area))

