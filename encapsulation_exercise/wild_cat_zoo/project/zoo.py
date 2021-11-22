from encapsulation_exercise.wild_cat_zoo.project.animal import Animal
from encapsulation_exercise.wild_cat_zoo.project.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if self.__animal_capacity > len(self.animals) and self.__budget >= price:
            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        if self.__animal_capacity > len(self.animals) and self.__budget < price:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries = 0
        for worker in self.workers:
            salaries += worker.salary

        if self.__budget >= salaries:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        animals_expenses = 0
        for animal in self.animals:
            animals_expenses += animal.money_for_care

        if self.__budget >= animals_expenses:
            self.__budget -= animals_expenses
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = []
        tigers = []
        cheetahs = []
        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                lions.append(animal)
            elif animal.__class__.__name__ == "Tiger":
                tigers.append(animal)
            elif animal.__class__.__name__ == "Cheetah":
                cheetahs.append(animal)

        result = f"You have {len(self.animals)} animals"
        result += "\n" + f"----- {len(lions)} Lions:"
        for lion in lions:
            result += "\n" + str(lion)

        result += "\n" + f"----- {len(tigers)} Tigers:"
        for tiger in tigers:
            result += "\n" + str(tiger)

        result += "\n" + f"----- {len(cheetahs)} Cheetahs:"
        for cheetah in cheetahs:
            result += "\n" + str(cheetah)
        return result

    def workers_status(self):
        keepers = []
        caretakers = []
        vets = []
        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                keepers.append(worker)
            elif worker.__class__.__name__ == "Caretaker":
                caretakers.append(worker)
            elif worker.__class__.__name__ == "Vet":
                vets.append(worker)

        result = f"You have {len(self.workers)} workers"
        result += "\n" + f"----- {len(keepers)} Keepers:"
        for keeper in keepers:
            result += "\n" + str(keeper)

        result += "\n" + f"----- {len(caretakers)} Caretakers:"
        for caretaker in caretakers:
            result += "\n" + str(caretaker)

        result += "\n" + f"----- {len(vets)} Vets:"
        for vet in vets:
            result += "\n" + str(vet)
        return result















