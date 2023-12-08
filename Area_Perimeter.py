class Circle:
    # Class variable (private) for pi
    __pi = 3.141

    def __init__(self, radius_list):
        # Instance variable to store the list of radii
        self.radius_list = radius_list

    def calculate_area(self, radius):
        # Class method to calculate the area of a circle
        return Circle.__pi * (radius ** 2)

    def calculate_perimeter(self, radius):
        # Class method to calculate the perimeter (circumference) of a circle
        return 2 * Circle.__pi * radius

radius_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle_instance = Circle(radius_list)

# Example of using class methods for each radius in the list
for radius in radius_list:
    area = circle_instance.calculate_area(radius)
    perimeter = circle_instance.calculate_perimeter(radius)

    print(f"For radius {radius}:")
    print("Area:", area)
    print("Perimeter:", perimeter)
    print()
