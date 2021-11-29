from static_and_class_methods_lab.hotel_rooms.project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if (
                    room.number == room_number and
                    not room.is_taken and
                    room.capacity >= people
            ):
                room.is_taken = True
                room.guests += people
                self.guests += people

    def free_room(self, room_number):
        for room in self.rooms:
            if (
                    room.number == room_number and
                    room.is_taken
            ):
                room.is_taken = False
                self.guests -= room.guests
                room.guests = 0

    def status(self):
        return f"""Hotel {self.name} has {self.guests} total guests
Free rooms: {', '.join([str(room.number) for room in self.rooms if not room.is_taken])}
Taken rooms: {', '.join([str(room.number) for room in self.rooms if room.is_taken])}
"""
