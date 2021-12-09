from OOP_exam_23_08_21.project.astronaut.astronaut_repository import AstronautRepository
from OOP_exam_23_08_21.project.astronaut.biologist import Biologist
from OOP_exam_23_08_21.project.astronaut.geodesist import Geodesist
from OOP_exam_23_08_21.project.astronaut.meteorologist import Meteorologist
from OOP_exam_23_08_21.project.planet.planet import Planet
from OOP_exam_23_08_21.project.planet.planet_repository import PlanetRepository


# from project.astronaut.astronaut_repository import AstronautRepository
# from project.astronaut.biologist import Biologist
# from project.astronaut.geodesist import Geodesist
# from project.astronaut.meteorologist import Meteorologist
# from project.planet.planet import Planet
# from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    ASTRONAUT_TYPES = {"Biologist", "Geodesist", "Meteorologist"}

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type not in self.ASTRONAUT_TYPES:
            raise Exception("Astronaut type is not valid!")

        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."

        if astronaut_type == Biologist.__name__:
            new_astronaut = Biologist(name)
            self.astronaut_repository.add(new_astronaut)
            return f"Successfully added {astronaut_type}: {name}."

        elif astronaut_type == Geodesist.__name__:
            new_astronaut = Geodesist(name)
            self.astronaut_repository.add(new_astronaut)
            return f"Successfully added {astronaut_type}: {name}."

        elif astronaut_type == Meteorologist.__name__:
            new_astronaut = Meteorologist(name)
            self.astronaut_repository.add(new_astronaut)
            return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."
        new_planet = Planet(name)
        new_planet.items = items.split(", ")
        self.planet_repository.add(new_planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut is not None:
            self.astronaut_repository.remove(astronaut)
            return f"Astronaut {name} was retired!"
        raise Exception(f"Astronaut {name} doesn't exist!")

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        pass

    def report(self):
        pass




