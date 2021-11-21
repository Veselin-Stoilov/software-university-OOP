from encapsulation_exercise.pizza_maker.project.dough import Dough
from encapsulation_exercise.pizza_maker.project.topping import Topping


class Pizza:
    def __init__(self, name, dough: Dough, topping_capacity):
        self.name = name
        self.dough = dough
        self.toppings_capacity = topping_capacity
        self.toppings = {}  # {topping_type: weight}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("The name cannot be an empty string")
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value

    @property
    def toppings_capacity(self):
        return self.__topping_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        if value <= 0:
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        self.__topping_capacity = value

    def add_topping(self, topping: Topping):
        if len(self.toppings) == self.toppings_capacity:
            raise ValueError("Not enough space for another topping")

        if topping.topping_type not in self.toppings:
            self.toppings[topping.topping_type] = 0
        self.toppings[topping.topping_type] += topping.weight

    def calculate_total_weight(self):
        toppings_weight = 0
        for topping in self.toppings:
            toppings_weight += self.toppings[topping]
        total_weight = self.dough.weight + toppings_weight
        return total_weight





