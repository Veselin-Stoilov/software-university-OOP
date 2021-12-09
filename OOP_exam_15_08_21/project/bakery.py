from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []  # food objects
        self.drinks_menu = []  # drinks objects
        self.table_repository = []  # table objects
        self.table_income = 0  # total income from all completed bills

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        for food in self.food_menu:
            if food.name == name:
                return f"{food_type} {name} is already in the menu!"

        if food_type == "Bread":
            new_food = Bread(name, price)
            self.food_menu.append(new_food)
            return f"Added {name} ({food_type}) to the food menu"

        if food_type == "Cake":
            new_food = Cake(name, price)
            self.food_menu.append(new_food)
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink (self, drink_type: str, name: str, portion: float, brand: str):
        for drink in self.drinks_menu:
            if drink.name == name:
                return f"{drink_type} {name} is already in the menu!"

        if drink_type == "Water":
            new_food = Water(name, portion, brand)
            self.drinks_menu.append(new_food)
            return f"Added {name} ({brand}) to the drink menu"

        if drink_type == "Tea":
            new_food = Tea(name, portion, brand)
            self.drinks_menu.append(new_food)
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        for table in self.table_repository:
            if table.table_number == table_number:
                raise Exception(f"Table {table_number} is already in the bakery!")

        if table_type == "OutsideTable":
            new_table = OutsideTable(table_number, capacity)
            self.table_repository.append(new_table)
            return f"Added table number {table_number} in the bakery"

        if table_type == "InsideTable":
            new_table = InsideTable(table_number, capacity)
            self.table_repository.append(new_table)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.table_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table.is_reserved = True
                return f"Table {table.table_number} has been reserved for " \
                       f"{number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *args):  # food args, string

        food_not_on_menu = []  # strings
        table = self.object_by_number(table_number, self.table_repository)
        result = f"Table {table.table_number} ordered:"

        for food_name in args:
            food = self.object_by_name(food_name, self.food_menu)
            if food is None:
                food_not_on_menu.append(food_name)
            else:
                table.order_food(food)

        for food in table.food_orders:
            result += "\n" + f"- {food.name}: {food.portion}g - {food.price}lv"

        result += "\n" + f"{self.name} does not have in the menu:"
        for food in food_not_on_menu:
            result += "\n" + food
        return result

    def object_by_name(self, obj_name, objects):
        for obj in objects:
            if obj.name == obj_name:
                return obj
        return None

    def object_by_number(self, obj_number, objects):
        for obj in objects:
            if obj.table_number == obj_number:
                return obj
        return None

    def order_drink(self, table_number: int, *args):  # drinks args, string
        pass

    def leave_table(self, table_number: int):
        pass

    def get_free_tables_info(self):
        pass

    def get_total_income(self):
        pass

