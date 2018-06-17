
class Car(object): # Factory of cars --> Instance = object
   
    MAX_SPEED = 120
    MIN_SPEED = -20

    def __init__(self, color):
        self.color = color # Paint the car.
        # Add engine
        # Add wheels
        # Add Seats
        # Done

    def __repr__(self):
        return 'I am a happy car'

    def drive(self, speed):
        speed = min(speed, self.MAX_SPEED)
        speed = max(speed, self.MIN_SPEED)
        speed = 1.1*speed
        print('I am driving m/hr', speed)


# ---------------------------------------------------------------

myCar = Car('Blue') # Buy the car.
myCar.drive(90)
myCar.drive(45)
myCar.drive(190)
myCar.drive(445)
print(myCar)
print(myCar.color)
