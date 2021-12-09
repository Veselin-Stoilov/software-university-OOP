from OOP_exam_15_08_21.project.baked_food.baked_food import BakedFood
from OOP_exam_15_08_21.project.bakery import Bakery

bakery = Bakery("Gusto")
print(bakery.add_food("Bread", "Baguette", 15))
print(bakery.add_food("   ", "Bague", 15))
print(bakery.add_food("Cake", "Garaj", 10))
print(bakery.add_food("Cake", "Garaj", 10))
print(bakery.add_food("Cake", "Chokolate", 10))
print(bakery.add_drink("Tea", "Camomile", 20, "tea4you"))
print(bakery.add_drink("Water", "Sparkling", 25, "Ramlosa"))
print(bakery.add_drink("Water", "Sparkling", 25, "Ramlosa"))
print(bakery.add_table("OutsideTable", 55, 6))
print(bakery.add_table("OutsideTable", 53, 6))
print(bakery.add_table("InsideTable", 25, 6))
print(bakery.add_table("InsideTable", 34, 6))
print(bakery.reserve_table(3))
print(bakery.reserve_table(18))
print(bakery.order_food(25, "Baguette", "Chokolate", "MIlk"))


