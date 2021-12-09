from OOP_exam_23_08_21.project.space_station import SpaceStation
from OOP_exam_23_08_21.project.astronaut.biologist import Biologist
from OOP_exam_23_08_21.project.astronaut.geodesist import Geodesist

space_station = SpaceStation()
print(space_station.add_astronaut("Biologist", "Ivan"))
print(space_station.add_astronaut("Geodesist", "Ivo"))
print(space_station.add_planet("Mars", "1, 2, 3"))

print(space_station.add_planet("Mars", "1, 2, 3"))
print(space_station.retire_astronaut("Ivan"))
print(space_station.add_astronaut("Biologist", "Peter"))
print(space_station.add_astronaut("Meteorologist", "Pepo"))
print(space_station.add_astronaut("Geodesist", "Boncho"))
space_station.recharge_oxygen()
space_station.recharge_oxygen()
space_station.recharge_oxygen()

for astronaut in space_station.astronaut_repository.astronauts:
    astronaut.breath()
    print(astronaut.name)
    print(astronaut.oxygen)


