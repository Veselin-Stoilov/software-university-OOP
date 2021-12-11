from unittest import TestCase, main

from testing_exercise.hero.project.hero import Hero


class TestHero(TestCase):
    def test_vehicle_initialization(self):
        username = "Username"
        level = 10
        health = 15.5
        damage = 10.5

        hero = Hero(username, level, health, damage)

        self.assertEqual(username, hero.username)
        self.assertEqual(level, hero.level)
        self.assertEqual(health, hero.health)
        self.assertEqual(damage, hero.damage)

    def test_str_should_be_particular_string(self):
        username = "Username"
        level = 10
        health = 15.5
        damage = 10.5

        hero = Hero(username, level, health, damage)
        expected = f"Hero {hero.username}: {hero.level} lvl\n" \
                   f"Health: {hero.health}\n" \
                   f"Damage: {hero.damage}\n"
        actual = str(hero)
        self.assertEqual(expected, actual)

    def test_battle_when_enemy_hero_name_is_same_as_your_name_should_throw_exception(self):
        username1 = "Username1"
        level1 = 10
        health1 = 15.5
        damage1 = 10.5

        username2 = "Username1"
        level2 = 10
        health2 = 15.5
        damage2 = 10.5

        hero1 = Hero(username1, level1, health1, damage1)
        hero2 = Hero(username2, level2, health2, damage2)

        with self.assertRaises(Exception) as context:
            hero1.battle(hero2)

        expected = "You cannot fight yourself"
        actual = str(context.exception)

        self.assertEqual(expected, actual)

    def test_battle_when_health_less_than_zero_should_throw_value_error(self):
        username1 = "Username1"
        level1 = 10
        health1 = -1
        damage1 = 10.5

        username2 = "Username2"
        level2 = 10
        health2 = 15.5
        damage2 = 10.5

        hero1 = Hero(username1, level1, health1, damage1)
        hero2 = Hero(username2, level2, health2, damage2)

        with self.assertRaises(ValueError) as context:
            hero1.battle(hero2)

        expected = "Your health is lower than or equal to 0. You need to rest"
        actual = str(context.exception)

        self.assertEqual(expected, actual)

    def test_battle_when_health_equal_to_zero_should_throw_value_error(self):
        username1 = "Username1"
        level1 = 10
        health1 = 0
        damage1 = 10.5

        username2 = "Username2"
        level2 = 10
        health2 = 15.5
        damage2 = 10.5

        hero1 = Hero(username1, level1, health1, damage1)
        hero2 = Hero(username2, level2, health2, damage2)

        with self.assertRaises(ValueError) as context:
            hero1.battle(hero2)

        expected = "Your health is lower than or equal to 0. You need to rest"
        actual = str(context.exception)

        self.assertEqual(expected, actual)

    def test_battle_when_enemy_health_less_than_zero_should_throw_value_error(self):
        username1 = "Username1"
        level1 = 10
        health1 = 28
        damage1 = 10.5

        username2 = "Username2"
        level2 = 10
        health2 = -1
        damage2 = 10.5

        hero1 = Hero(username1, level1, health1, damage1)
        hero2 = Hero(username2, level2, health2, damage2)

        with self.assertRaises(ValueError) as context:
            hero1.battle(hero2)

        expected = f"You cannot fight {hero2.username}. He needs to rest"
        actual = str(context.exception)

        self.assertEqual(expected, actual)

    def test_battle_when_enemy_health_less_than_zero_should_throw_value_error(self):
        username1 = "Username1"
        level1 = 10
        health1 = 28
        damage1 = 10.5

        username2 = "Username2"
        level2 = 10
        health2 = 0
        damage2 = 10.5

        hero1 = Hero(username1, level1, health1, damage1)
        hero2 = Hero(username2, level2, health2, damage2)

        with self.assertRaises(ValueError) as context:
            hero1.battle(hero2)

        expected = f"You cannot fight {hero2.username}. He needs to rest"
        actual = str(context.exception)

        self.assertEqual(expected, actual)

    def test_battle_when_enemy_health_and_your_health_less_than_zero_should_return_str(self):
        username1 = "Username1"
        level1 = 10
        health1 = 28
        damage1 = 100

        username2 = "Username2"
        level2 = 10
        health2 = 2
        damage2 = 100

        hero1 = Hero(username1, level1, health1, damage1)
        hero2 = Hero(username2, level2, health2, damage2)

        expected = "Draw"
        actual = hero1.battle(hero2)

        self.assertEqual(expected, actual)

    def test_battle_when_after_damage_enemy_health_and_your_health_equal_to_zero_should_return_str(self):
        username1 = "Username1"
        level1 = 10
        health1 = 1000
        damage1 = 100

        username2 = "Username2"
        level2 = 10
        health2 = 1000
        damage2 = 100

        hero1 = Hero(username1, level1, health1, damage1)
        hero2 = Hero(username2, level2, health2, damage2)

        expected = "Draw"
        actual = hero1.battle(hero2)

        self.assertEqual(expected, actual)

    def test_battle_when_after_damage_enemy_health_less_than_zero_should_return_str(self):
        username1 = "Username1"
        level1 = 10
        health1 = 2800
        damage1 = 100

        username2 = "Username2"
        level2 = 10
        health2 = 2
        damage2 = 100

        hero1 = Hero(username1, level1, health1, damage1)
        hero2 = Hero(username2, level2, health2, damage2)

        expected = "You win"
        actual = hero1.battle(hero2)

        player_damage = damage1 * level1
        enemy_hero_damage = damage2 * level2

        health1 -= enemy_hero_damage
        health2 -= player_damage

        self.assertEqual(expected, actual)
        self.assertEqual(level1 + 1, hero1.level)
        self.assertEqual(health1 + 5, hero1.health)
        self.assertEqual(damage1 + 5, hero1.damage)

    def test_battle_when_after_damage_your_health_less_than_zero_should_return_str(self):
        username1 = "Username1"
        level1 = 10
        health1 = 28
        damage1 = 100

        username2 = "Username2"
        level2 = 10
        health2 = 2300
        damage2 = 100

        hero1 = Hero(username1, level1, health1, damage1)
        hero2 = Hero(username2, level2, health2, damage2)

        expected = "You lose"
        actual = hero1.battle(hero2)

        player_damage = damage1 * level1
        enemy_hero_damage = damage2 * level2

        health1 -= enemy_hero_damage
        health2 -= player_damage

        self.assertEqual(expected, actual)
        self.assertEqual(level2 + 1, hero2.level)
        self.assertEqual(health2 + 5, hero2.health)
        self.assertEqual(damage2 + 5, hero2.damage)





if __name__ == "__main__":
    main()