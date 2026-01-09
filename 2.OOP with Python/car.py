
class car:

    def __init__(self, make, model, color, year):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.is_running = False
    

    def start(self):
        self.is_running = True
        print(f"The {self.year} {self.make} {self.model} {self.color} is now running.")


    def stop(self):
        self.is_running = False
        print(f"The {self.year} {self.make} {self.model} {self.color} has stopped.")


    def display_info(self):
        status = "running" if self.is_running else "not running"
        print(f"{self.year} {self.make} {self.model} {self.color} is currently {status}.")

class flying_car(car):
    def __init__ (self, make, model, color, year, flyingtype):
        super().__init__(make, model, color, year)
        self.flyingtype = flyingtype
    
    def details(self):
        return f"{self.year} {self.make} {self.model} {self.color} is {self.flyingtype}."

car1 = car("Toyota", "Camry", "yellow", 2022)
car2 = car("Honda", "Civic", "white", 2020)
flying1 = flying_car("yeah")
flying2 = flying_car("hooo")

car1.display_info()
car1.start()
car1.display_info()
car1.stop()
car1.details()

car2.display_info()