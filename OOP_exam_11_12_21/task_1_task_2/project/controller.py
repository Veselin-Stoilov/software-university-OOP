# from OOP_exam_11_12_21.task_1_task_2.project.race import Race
from OOP_exam_11_12_21.task_1_task_2.project.car.muscle_car import MuscleCar
from OOP_exam_11_12_21.task_1_task_2.project.car.sports_car import SportsCar
from OOP_exam_11_12_21.task_1_task_2.project.driver import Driver
from OOP_exam_11_12_21.task_1_task_2.project.race import Race


class Controller:
    def __init__(self):  # TODO may be some of the attributes should be assigned to other classes
        self.cars = []  # add all cars as OBJECTS
        self.drivers = []  # add all drives as OBJECTS
        self.races = []  # add all races as OBJECTS

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if self.car_model_already_exists(model, self.cars):
            raise Exception(f"Car {model} is already created!")

        if car_type == "MuscleCar":
            new_car = MuscleCar(model, speed_limit)
            self.cars.append(new_car)
            return f"{car_type} {model} is created."

        if car_type == "SportsCar":
            new_car = SportsCar(model, speed_limit)
            self.cars.append(new_car)
            return f"{car_type} {model} is created."

    def car_model_already_exists(self, model, cars):  # finds the car model if it was already created
        for car in cars:
            if car.model == model:
                return True
        return False

    def create_driver(self, driver_name: str):
        if self.find_obj_by_name(driver_name, self.drivers):
            raise Exception(f"Driver {driver_name} is already created!")
        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def find_obj_by_name(self, name, objects):  # finds the object name if it was already created
        for obj in objects:
            if obj.name == name:
                return obj
        return None

    def create_race(self, race_name: str):
        if self.find_obj_by_name(race_name, self.races):
            raise Exception(f"Race {race_name} is already created!")

        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.find_obj_by_name(driver_name, self.drivers)
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        new_car = self.find_last_car_of_type(car_type, self.cars)
        if new_car is None or new_car.is_taken:
            raise Exception(f"Car {car_type} could not be found!")

        if driver.car is not None:
            old_car = driver.car
            return f"Driver {driver.name} changed his car from {old_car.model} to {new_car.model}."

        driver.car = new_car
        return f"Driver {driver.name} chose the car {new_car.model}."

    def find_last_car_of_type(self, car_type, cars):  # returns the car of the given type
        for car in cars[::-1]:
            if car.__class__.__name__ == car_type:
                return car
        return None

    def add_driver_to_race(self, race_name: str, driver_name: str):
        driver = self.find_obj_by_name(driver_name, self.drivers)
        race = self.find_obj_by_name(race_name, self.races)

        if race is None:
            raise Exception(f"Race {race_name} could not be found!")

        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        pass







