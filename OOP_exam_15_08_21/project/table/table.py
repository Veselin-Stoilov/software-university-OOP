from abc import ABC, abstractmethod

from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink


class Table(ABC):
    @abstractmethod
    def __init__(self, table_number, capacity):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    def reserve(self, number_of_people: int):
        self.is_reserved = True
        self.number_of_people = number_of_people

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        result = 0
        for drink in self.drink_orders:
            result += drink.price
        for food in self.food_orders:
            result += food
        return result

    def clear(self):
        self.food_orders.clear()
        self.drink_orders.clear()
        self.number_of_people = 0
        self.is_reserved = False  # To Do: may be should not be changed

    def free_table_info(self):
        if not self.is_reserved:
            result = f"Table: {self.table_number}\n" \
                     f"Type: {self.__class__.__name__}\n" \
                     f"Capacity: {self.capacity}"
            return result








