# Define the Circle class
class Circle:
    def __init__(self, radius_list):
        # Initialize the private variable __pi with the value 3.141
        self.__pi = 3.141
        # Initialize the instance variable radius_list with the provided list
        self.radius_list = radius_list

    def get_pi(self):
        # Method to access the private variable __pi
        return self.__pi

radius_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle_instance = Circle(radius_list)

# printing the radius_list and pi
print("Radius List:", circle_instance.radius_list)
print("Value of pi:", circle_instance.get_pi())
