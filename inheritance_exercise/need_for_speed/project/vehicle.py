class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25  # liters/km

    def __init__(self, fuel, horse_power):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = 1.25
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers):
        max_distance = self.fuel / self.fuel_consumption
        if max_distance >= kilometers:
            self.fuel -= kilometers * self.fuel_consumption

