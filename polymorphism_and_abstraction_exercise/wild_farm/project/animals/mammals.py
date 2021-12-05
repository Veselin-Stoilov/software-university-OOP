from polymorphism_and_abstraction_exercise.wild_farm.project.animals.animal import Mammal


class Mouse(Mammal):
    food = ["Vegetable", "Fruit"]

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if food.__name__ not in self.food:
            return f"{self.__class__.__name__} does not eat {food.__name__}!"
        self.weight += food.quantity * 0.1


class Dog(Mammal):
    food = ["Meat"]

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if food.__class__.__name__ not in self.food:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * 0.4
        self.food_eaten += food.quantity


class Cat(Mammal):
    food = ["Vegetable", "Meat"]

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if food.__class__.__name__ not in self.food:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * 0.30
        self.food_eaten += food.quantity


class Tiger(Mammal):
    food = ["Meat"]

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if food.__class__.__name__ not in self.food:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity
        self.food_eaten += food.quantity
