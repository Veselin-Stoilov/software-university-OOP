from project.table.table import Table


class InsideTable(Table):
    def __init__(self, table_number, capacity):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if value not in range(1, 51):
            raise ValueError("Inside table's number must be between 1 and 50 inclusive!")
        self.__table_number = value
