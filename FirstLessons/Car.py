# Car class file

class Car:
    
    
    # Class variable
    wheels = 4
    
    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    
    def drive(self):
        print("This "+ self.model+" car is driving")
        
    def stop(self):
        print("The "+ self.model+" car has stopped")