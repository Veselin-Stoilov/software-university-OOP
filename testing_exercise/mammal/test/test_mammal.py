from unittest import TestCase, main

from testing_exercise.mammal.project.mammal import Mammal


class TestMammal(TestCase):
    def test_mammal_initialization(self):
        name = "name"
        mammal_type = "type"
        sound = "sound"
        kingdom = "animals"

        mammal = Mammal(name, mammal_type, sound)

        self.assertEqual(name, mammal.name)
        self.assertEqual(mammal_type, mammal.type)
        self.assertEqual(sound, mammal.sound)
        self.assertEqual(kingdom, mammal._Mammal__kingdom)

    def test_make_sound_should_return_given_string(self):
        name = "name"
        mammal_type = "type"
        sound = "sound"
        kingdom = "animals"

        mammal = Mammal(name, mammal_type, sound)

        expected = f"{mammal.name} makes {mammal.sound}"
        actual = mammal.make_sound()

        self.assertEqual(expected, actual)

    def test_get_kingdom_should_return_kingdom(self):
        name = "name"
        mammal_type = "type"
        sound = "sound"
        kingdom = "animals"

        mammal = Mammal(name, mammal_type, sound)

        expected = kingdom
        actual = mammal.get_kingdom()

        self.assertEqual(expected, actual)

    def test_info_should_return_given_string(self):
        name = "name"
        mammal_type = "type"
        sound = "sound"
        kingdom = "animals"

        mammal = Mammal(name, mammal_type, sound)

        expected = f"{mammal.name} is of type {mammal.type}"
        actual = mammal.info()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()
