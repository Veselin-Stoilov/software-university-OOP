from project.baked_food.baked_food import BakedFood


class Bread(BakedFood):
    def __init__(self, name, price):
        self.name = name
        self.portion = 200
        self.price = price



