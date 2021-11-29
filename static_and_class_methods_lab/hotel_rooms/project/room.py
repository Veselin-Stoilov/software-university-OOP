class Room:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def _can_take_room(self, people):
        return not self.is_taken and self.capacity >= people

    def take_room(self, people):
        if self._can_take_room(people):
            self.is_taken = True
            self.guests += people
            return
        return f"Room number {self.number} cannot be taken"

    def free_room(self):
        if self.is_taken:
            self.is_taken = False
            self.guests = 0
            return
        return f"Room number {self.number} is not taken"


