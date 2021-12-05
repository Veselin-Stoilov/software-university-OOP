from polymorphism_and_abstraction_exercise.wild_farm.project.animals.animal import Bird
from polymorphism_and_abstraction_exercise.wild_farm.project.food import Food


class Owl(Bird):
    food = ["Meat"]

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if food.__class__.__name__ not in self.food:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * 0.25
        self.food_eaten += food.quantity


class Hen(Bird):
    food = ["Vegetable", "Fruit", "Meat", "Seed"]

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    def feed(self, food: Food):
        if food.__class__.__name__ not in self.food:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * 0.35
        self.food_eaten += food.quantity


