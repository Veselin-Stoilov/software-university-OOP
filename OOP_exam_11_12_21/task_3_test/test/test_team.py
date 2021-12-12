from unittest import TestCase, main

from OOP_exam_11_12_21.task_3_test.project.team import Team


class TestTeam(TestCase):
    def test_team_initialization(self):
        name = "Name"
        members = {}

        team = Team(name)

        self.assertEqual(name, team.name)
        self.assertTrue(isinstance(team.members, dict))

    def test_name_is_alpha_should_throw_value_error(self):
        name = "Name1"
        members = {}

        with self.assertRaises(ValueError) as context:
            team = Team(name)

        expected = "Team Name can contain only letters!"
        actual = str(context.exception)

        self.assertEqual(expected, actual)

    def test_add_member_function(self):
        name = "Name"
        # members = {"Ivan": 16, "Peter": 18}

        team = Team(name)
        team.add_member(Stoyan=20, Petkan=23)
        added_members_by_name = ["Stoyan", "Petkan"]

        expected = 2
        actual = len(team.members)

        self.assertEqual(expected, actual)

    def test_add_member_return_message(self):
        name = "Name"
        # members = {"Ivan": 16, "Peter": 18}

        team = Team(name)

        added_members_by_name = ["Stoyan", "Petkan"]

        expected_result = f"Successfully added: {', '.join(added_members_by_name)}"
        actual_result = team.add_member(Stoyan=20, Petkan=23)

        self.assertEqual(expected_result, actual_result)
        self.assertTrue("Stoyan" in team.members)
        self.assertTrue("Petkan" in team.members)

    def test_remove_member_when_member_does_not_exist_should_return_particular_string(self):
        name = "Name"
        wrong_name_to_remove = "PeterPeter"
        team = Team(name)
        team.members = {"Ivan": 16, "Peter": 18}

        expected = f"Member with name {wrong_name_to_remove} does not exist"
        actual = team.remove_member(wrong_name_to_remove)

        self.assertEqual(expected, actual)

    def test_remove_member_when_member_exists_should_return_particular_string_and_remove_him(self):
        name = "Name"
        correct_name_to_remove = "Peter"
        team = Team(name)
        team.members = {"Ivan": 16, "Peter": 18}

        expected = f"Member {correct_name_to_remove} removed"
        actual = team.remove_member(correct_name_to_remove)
        is_removed = "Peter" not in team.members

        self.assertTrue(is_removed)
        self.assertEqual(expected, actual)
        self.assertEqual(1, len(team.members))

    def test_remove_member_when_member_exists_should_remove_them(self):
        name = "Name"
        correct_name_to_remove = "Peter"
        team = Team(name)
        team.members = {"Ivan": 16, "Peter": 18}

        team.remove_member(correct_name_to_remove)

        self.assertFalse(correct_name_to_remove in team.members)

    def test_greater_than_should_return_True(self):
        name = "Name"
        name_other = "Other"
        team = Team(name)
        team_other = Team(name_other)
        team.members = {"Ivan": 16, "Peter": 18}
        team_other.members = {"A": 16}

        expected = True
        actual = (team > team_other)

        self.assertEqual(expected, actual)

    def test_greater_than_should_return_False(self):
        name = "Name"
        name_other = "Other"

        team = Team(name)
        team_other = Team(name_other)
        team.members = {"A": 16}
        team_other.members = {"Ivan": 16, "Peter": 18}

        expected = False
        actual = (team > team_other)

        self.assertEqual(expected, actual)

    def test_len_than_should_return_len_members(self):
        name = "Name"
        team = Team(name)
        team.members = {"Ivan": 16, "Peter": 18}

        expected = 2
        actual = len(team.members)

        self.assertEqual(expected, actual)

    def test_add_other_team_than_should_merge_names_and_members(self):
        name = "Name"
        name_other = "Other"

        team = Team(name)
        team_other = Team(name_other)
        team.members = {"A": 16}
        team_other.members = {"Ivan": 16, "Peter": 18}

        new_team_name = f"{team.name}{team_other.name}"

        expected_name = new_team_name
        new_team = team + team_other

        expected_members_len = 3
        actual_members_len = len(new_team.members)

        self.assertEqual(expected_name, new_team.name)
        self.assertEqual(expected_members_len, actual_members_len)

    def test_str__should_return_particular_string(self):
        name = "Name"
        team = Team(name)
        team.members = {"Ivan": 16, "Peter": 18}

        result = [f"Team name: {team.name}"]
        members = list(sorted(team.members.items(), key=lambda x: (-x[1], x[0])))
        result.extend([f"Member: {x[0]} - {x[1]}-years old" for x in members])

        expected = "\n".join(result)
        actual = str(team)

        self.assertEqual(expected, actual)



if __name__ == "__main__":
    main()