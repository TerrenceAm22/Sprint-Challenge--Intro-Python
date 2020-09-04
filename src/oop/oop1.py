# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
    """
    Base Class
    """
    pass


class GroundVehicle(Vehicle):
    """ 
    Inheriting from Vechicle Class
    """
    pass

class Car(GroundVehicle):
    """
    Inheriting from GroundVechicle
    """
    pass

class Motorcycle(GroundVehicle):
    """
    Inheriting from Ground Vechicle
    """
    pass


class FlightVehicle(Vehicle):
    """
    Inheriting from base class
    since this is a form a vechicle
    and so it would not share
    attributes from the ground vechicles class
    necessarily
    """
    pass

class Starship(FlightVehicle):
    """ 
    Inheriting from Flight class
    """
    pass

class Airplane(FlightVehicle):
    """
    Inheriting from flight class
    """
    pass

