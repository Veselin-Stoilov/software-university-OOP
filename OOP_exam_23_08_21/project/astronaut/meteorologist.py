from OOP_exam_23_08_21.project.astronaut.astronaut import Astronaut

# from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    def __init__(self, name):
        super().__init__(name, 90)

    def breath(self):
        self.oxygen -= 15
