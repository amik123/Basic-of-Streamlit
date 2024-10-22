# class Car:
#     def __init__(self,doors,windows,enginetype) -> None:
#         self.doors=doors
#         self.windows=windows
#         self.enginetype=enginetype
    
#     def specs(self):
#         print(f'this car has {self.doors} doors, {self.windows} windows')

#     def drive(self):
#         print(f'it is {self.enginetype} car')

# class Tesla(Car):
#     def __init__(self,isselfdrive) -> None:
#         self.isselfdrive=isselfdrive
#         super().__init__()

# car1=Tesla(True)
# car1.specs()

###Multiple Inheritance

class Car:
    def __init__(self,windows,doors,enginetype) -> None:
        self.windows=windows
        self.doors=doors
        self.enginetype=enginetype

    def engine(self):
        """The day when things get """
        print(f"we are driving {self.enginetype} engine")
    
class Winger:
    def __init__(self,tyres,seats) -> None:
        self.tyres=tyres
        self.seats=seats
        
class Tesla(Car,Winger):
    def __init__(self,windows,doors,enginetype,tyres,seats,is_comfort):
        Winger.__init__(self,tyres,seats)
        Car.__init__(self,windows,doors,enginetype)
        self.is_comfort=is_comfort

tesla1=Tesla(4,3,'Petrol',4,7,True)
tesla1.engine()

"""The day when things get """