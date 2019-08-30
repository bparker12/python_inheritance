class Vehicle:

    def __init__(self, engine, color, tires, make, model):
        self.engine = engine
        self.color = color
        self.tire_num = tires
        self.make = make
        self. model = model

    def drive(self, noise):
        print(f'The {self.color} {self.model} drives past.{noise}')

    def turn(self, direction):
        print(f'The {self.make} {self.model} turns {direction} to avoid the person ahead')

    def stop(self, direction):
        print(f'The {self.make} {self.model} turns {direction} to avoid the person ahead')

class Car(Vehicle):
    def __init__(self, style):
        self.style = style
        super().__init__("EJ20", "black", 4, "Subaru", "WRX-STI S207")

    def move(self):
        return self.drive("vrrooooommmmm")
    def right(self):
        return self.turn("right")
    def slow(self):
        return self.stop("stop")

class Truck(Vehicle):
    def __init__(self, style):
        self.style = style
        super().__init__("3.5 L V-6", "black", 4, "Toyota", "Tocoma")

    def move(self):
        return self.drive("ruuuummmmmbbbblllleeee")

class Plane(Vehicle):
    def __init__(self, wing):
        self.wing = wing
        super().__init__("General Electric Passport", "black", 3, "Bombardier", "Global 8000")

    def move(self):
        return self.drive("vvvvwooooooossshhhhhh")

class Motorcyle(Vehicle):
    def __init__(self, drive):
        self.drive = drive
        super().__init__("1,043 cc (63.6 cu in) liquid-cooled 4-stroke 16-valve DOHC inline-four", "red", 2, "Kawasaki", "Ninja 1000")

    def move(self):
        return self.drive("waaaaaaaaaaaooohhhhhhhhhh")


class Suv(Vehicle):
    def __init__(self, tow=False):
        self.tow = tow
        super().__init__("2.9 L Cologne V6", "white", 4, "Ford", "Bronco II")

    def move(self):
        return self.drive("gggggggggdddddddddddddrrrrrrrrrrr")

subaru = Car("sport")

subaru.move()
subaru.right()
subaru.slow()