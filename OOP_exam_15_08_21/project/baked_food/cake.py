from project.baked_food.baked_food import BakedFood


class Cake(BakedFood):
    def __init__(self, name, price):
        self.name = name
        self.portion = 245
        self.price = price
