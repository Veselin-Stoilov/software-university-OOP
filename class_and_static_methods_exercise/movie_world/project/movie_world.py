from class_and_static_methods_exercise.movie_world.project.customer import Customer
from class_and_static_methods_exercise.movie_world.project.dvd import DVD


class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []  # customers objects
        self.dvds = []  # dvd objects

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        for dvd in self.dvds:
            if dvd_id == dvd.id:
                for customer in self.customers:
                    if customer_id == customer.id:
                        if dvd.is_rented:
                            if dvd in customer.rented_dvds:
                                return f"{customer.name} has already rented {dvd.name}"
                            return "DVD is already rented"
                        if dvd.age_restriction > customer.age:
                            return f"{customer.name} should be at least " \
                                   f"{dvd.age_restriction} to rent this movie"

                        dvd.is_rented = True
                        customer.rented_dvds.append(dvd)
                        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        for customer in self.customers:
            if customer.id == customer_id:
                for dvd in customer.rented_dvds:
                    if dvd.id == dvd_id:
                        customer.rented_dvds.remove(dvd)
                        dvd.is_rented = False
                        return f"{customer.name} has successfully returned {dvd.name}"
                return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = ''
        for customer in self.customers:
            result += str(customer) + "\n"
        for dvd in self.dvds:
            result += str(dvd) + "\n"
        return result.strip()


