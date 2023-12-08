class TV:
    def __init__(self, brand):
        self.brand = brand
        self.channel = 1
        self.price = 45000  
        self.inches = 43  
        self.on_off_status = False
        self.volume = 50

    def increase_volume(self):
        self.volume = min(100, self.volume + 1)

    def decrease_volume(self):
        self.volume = max(0, self.volume - 1)

    def set_channel(self, new_channel):
        self.channel = min(50, max(1, new_channel))  # Limit channel to 1-50


    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"


class LedTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = 0  
        self.backlight = False  

    def display_details(self):
        return f"{self.brand} - Screen Thickness: {self.screen_thickness}, Energy Usage: {self.energy_usage}, Lifespan: {self.lifespan}, Refresh Rate: {self.refresh_rate}, Viewing Angle: {self.viewing_angle}, Backlight: {'On' if self.backlight else 'Off'}"


class PlasmaTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = 0  
        self.backlight = False  

    def display_details(self):
        return f"{self.brand} - Screen Thickness: {self.screen_thickness}, Energy Usage: {self.energy_usage}, Lifespan: {self.lifespan}, Refresh Rate: {self.refresh_rate}, Viewing Angle: {self.viewing_angle}, Backlight: {'On' if self.backlight else 'Off'}"


# Example usage:
led_tv = LedTV("Panasonic", "Slim", "Low", "Long", "120Hz")
plasma_tv = PlasmaTV("Samsung", "Thick", "High", "Medium", "60Hz")

# Part A
print(led_tv.status())  # Output: Panasonic at channel 1, volume 50
print(plasma_tv.status())  # Output: Samsung at channel 1, volume 50


# Part B
print(led_tv.display_details())
print(plasma_tv.display_details())
