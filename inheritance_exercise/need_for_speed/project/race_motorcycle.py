from inheritance_exercise.need_for_speed.project.motorcycle import Motorcycle


class RaceMotorcar(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)