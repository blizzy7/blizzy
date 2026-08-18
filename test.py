# class KioskMachine:
#     pass

# print(KioskMachine)

# class CoffeeCup:
#     pass

# # Stamp out two separate cup instances from the blueprint
# cup_1 = CoffeeCup()
# cup_2 = CoffeeCup()

# print(type(cup_1)) # Output: <class '__main__.CoffeeCup'>
# class CardboardCup:
# def __init__(self, size):
#     self.size = size
#     self.is_steamed = False
        
#     # An instance method that operates on the cup
# def steam_cup(self):
#     self.is_steamed = True
# print(f"The {self.size} cup is now steamed and warm.")
# class Cup:
#     def check_self(self):
#         print(self)

# my_cup = Cup()
# print(my_cup)
# my_cup.check_self()
# class CardboardCup:
#     def __init__(self, capacity):
#         self.capacity_ounces = capacity
#         self.contents_ounces = 0.0
        
#     def fill(self, ounces):
#         # Modify the attribute in-place using addition assignment
#         self.contents_ounces += ounces
#         print(f"Filled cup with {ounces} ounces of coffee.")

# my_cup = CardboardCup(12.0)
# my_cup.fill(8.0)
class CardboardCup:
    def __init__(self, capacity):
        self.capacity_ounces = capacity
        self.contents_ounces = 0.0
        
    def fill(self, ounces):
        # Safety Gate: check if pouring would cause an overflow
        if self.contents_ounces + ounces > self.capacity_ounces:
            print("Action Blocked: Spill Warning! This will overflow.")
        else:
            self.contents_ounces += ounces
            print(f"Successfully filled cup. Current level: {self.contents_ounces} oz")