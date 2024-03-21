"""TASK 1"""
# class Car:
#     def __init__(self, max_speed, speed_unit):
#         self.max_speed = max_speed
#         self.speed_unit = speed_unit

#     def __str__(self):
#         return f"Car with the maximum speed of {self.max_speed} {self.speed_unit}"

# class Boat:
#     def __init__(self, max_speed):
#         self.max_speed = max_speed
#     def __str__(self):
#         return f"Boat with the maximum speed of {self.max_speed} knots"

# car = Car(max_speed=55, speed_unit="km/h")
# print(car)

"""TASK 2"""
class Item:
    # Implement the Item here
    pass
    def __init__(self, name:str, price:int):
        self.name = name
        self.price = price
    '''>>> bike price'''

# item = Item(name="apple", price=5000)
# print(item.name, item.price)
class ShoppingCart:
    # Implement the ShoppingCart here
    def __init__(self):
        self.objects = []
   
    def add(self, item):
        self.objects.append(item)
        

    def total(self):
        return sum([item.price for item in self.objects])

    def __len__(self):
        return len(self.objects)

    
item1 = Item(name="bike", price=1000)
item2 = Item(name="headphone", price=100)
cart = ShoppingCart()
cart.add(item1)
# print(cart)
cart.add(item2)
print(cart.total())
print(len(cart))
