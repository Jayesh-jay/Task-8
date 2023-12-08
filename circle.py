# Define the Circle class
class Circle:
    def __init__(self, radius_list):
        # Initialize the instance variable radius_list with the provided list
        self.radius_list = radius_list

radius_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle_instance = Circle(radius_list)

# printing the radius_list
print("Radius List:", circle_instance.radius_list)
