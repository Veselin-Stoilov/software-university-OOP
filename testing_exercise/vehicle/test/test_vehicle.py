from unittest import TestCase, main

from testing_exercise.vehicle.project.vehicle import Vehicle


class TestVehicle(TestCase):
    def test_vehicle_initialization(self):
        DEFAULT_FUEL_CONSUMPTION = 1.25

        fuel = 5.0
        capacity = fuel
        horse_power = 10.0
        fuel_consumption = DEFAULT_FUEL_CONSUMPTION

        vehicle = Vehicle(fuel, horse_power)

        self.assertEqual(fuel, vehicle.fuel)
        self.assertEqual(capacity, vehicle.capacity)
        self.assertEqual(horse_power, vehicle.horse_power)
        self.assertEqual(fuel_consumption, vehicle.fuel_consumption)

    def test_vehicle_str_should_return_proper_string(self):
        DEFAULT_FUEL_CONSUMPTION = 1.25

        fuel = 5.0
        capacity = fuel
        horse_power = 10.0
        fuel_consumption = DEFAULT_FUEL_CONSUMPTION

        vehicle = Vehicle(fuel, horse_power)
        expected = f"The vehicle has {vehicle.horse_power} horse power with " \
                   f"{vehicle.fuel} fuel left and {vehicle.fuel_consumption} fuel consumption"

        actual = str(vehicle)

        self.assertEqual(expected, actual)

    def test_drive_when_fuel_is_less_then_needed_fuel_it_should_raise_exception(self):
        DEFAULT_FUEL_CONSUMPTION = 1.25
        fuel = 5.0
        capacity = fuel
        horse_power = 10.0
        fuel_consumption = DEFAULT_FUEL_CONSUMPTION
        kilometers = 100

        vehicle = Vehicle(fuel, horse_power)

        with self.assertRaises(Exception) as context:
            vehicle.drive(kilometers)
        expected = "Not enough fuel"
        actual = str(context.exception)

        self.assertEqual(expected, actual)

    def test_drive_when_needed_fuel_is_enough_it_should_reduce_the_fuel(self):
        DEFAULT_FUEL_CONSUMPTION = 1.25

        fuel = 100.0
        capacity = fuel
        horse_power = 10.0
        fuel_consumption = DEFAULT_FUEL_CONSUMPTION
        kilometers = 5

        vehicle = Vehicle(fuel, horse_power)
        fuel_needed = fuel_consumption * kilometers
        fuel -= fuel_needed

        vehicle.drive(kilometers)
        expected = fuel
        actual = vehicle.fuel
        self.assertEqual(expected, actual)

    def test_refuel_when_recharged_fuel_more_than_capacity_should_raise_exception(self):
        DEFAULT_FUEL_CONSUMPTION = 1.25

        fuel = 5.0
        capacity = fuel
        horse_power = 10.0
        fuel_consumption = DEFAULT_FUEL_CONSUMPTION
        kilometers = 100
        recharged_fuel = capacity + 1

        vehicle = Vehicle(fuel, horse_power)

        with self.assertRaises(Exception) as context:
            vehicle.refuel(recharged_fuel)
        self.assertEqual("Too much fuel", str(context.exception))

    def test_refuel_when_recharged_fuel_less_than_capacity_should_increase_fuel_level(self):
        DEFAULT_FUEL_CONSUMPTION = 1.25

        fuel = 5.0
        capacity = 20
        horse_power = 10.0
        fuel_consumption = DEFAULT_FUEL_CONSUMPTION
        kilometers = 100
        recharged_fuel = 1

        vehicle = Vehicle(fuel, horse_power)
        vehicle.capacity = 20
        vehicle.refuel(recharged_fuel)

        expected = fuel + recharged_fuel
        actual = vehicle.fuel
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()
