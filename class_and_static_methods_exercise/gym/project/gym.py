from class_and_static_methods_exercise.gym.project.customer import Customer
from class_and_static_methods_exercise.gym.project.equipment import Equipment
from class_and_static_methods_exercise.gym.project.exercise_plan import ExercisePlan
from class_and_static_methods_exercise.gym.project.subscription import Subscription
from class_and_static_methods_exercise.gym.project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = self.__get_obj_by_id(self.subscriptions, subscription_id)
        customer = self.__get_obj_by_id(self.customers, subscription.id)
        trainer = self.__get_obj_by_id(self.trainers, subscription.trainer_id)
        plan = self.__get_obj_by_id(self.plans, subscription.exercise_id)
        equipment = self.__get_obj_by_id(self.equipment, plan.equipment_id)

        result = str(subscription) + "\n"
        result += str(customer) + "\n"
        result += str(trainer) + "\n"
        result += str(equipment) + "\n"
        result += str(plan)

        return result

    @staticmethod
    def __get_obj_by_id(objects, obj_id):
        for obj in objects:
            if obj.id == obj_id:
                return obj

    # def subscription_info(self, subscription_id: int):
    #     result = ''
    #     for subscription in self.subscriptions:
    #         if subscription.id == subscription_id:
    #             result += str(subscription) + "\n"
    #
    #             for customer in self.customers:
    #                 if customer.id == subscription.id:
    #                     result += str(customer) + "\n"
    #
    #             for trainer in self.trainers:
    #                 if trainer.id == subscription.trainer_id:
    #                     result += str(trainer) + "\n"
    #
    #             for plan in self.plans:
    #                 if plan.id == subscription.exercise_id:
    #
    #                     for equipment in self.equipment:
    #                         if equipment.id == plan.equipment_id:
    #                             result += str(equipment) + "\n"
    #                             result += str(plan)
    #
    #     return result



