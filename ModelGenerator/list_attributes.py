from numpy import random

from ModelGenerator.Trainer import Trainer


class ListAttribute:
    # number_of_items: int = 0
    item_size_list: [int] = []
    item_intervals_list: [int] = []

    def __init__(self,
                 # number_of_items=0,
                 item_size_list=None, item_intervals_list=None):
        # self.number_of_items = number_of_items
        self.item_size_list = item_size_list
        self.item_intervals_list = item_intervals_list
        if self.item_intervals_list is None or self.item_size_list is None:
            # self.number_of_items = 0
            self.item_size_list = []
            self.item_intervals_list = []

    def train_list(self, size_distr, interval_distr, number_of_elements):
        # random_number = self.get_random_the_number_of_items()
        new_sizes = self.get_random_list(self.item_size_list, size_distr, number_of_elements)
        new_intervals = self.get_random_list(self.item_intervals_list, interval_distr, (number_of_elements - 1))

        return new_sizes, new_intervals

    def get_new_size(self, distr):
        return self.get_a_single_random_element(self.item_size_list, distr)

    def get_new_interval(self, distr):
        return self.get_a_single_random_element(self.item_intervals_list, distr)

    def get_random_the_number_of_items(self):
        rand_num = 0

        # todo use the specified distribution to get a random number
        rand_num = int(random.normal(loc=len(self.item_size_list), scale=3.0, size=None))
        assert isinstance(rand_num, int), 'Random number - wrong type!'

        if rand_num < 0:
            rand_num *= -1

        # todo know if rand_num == 0 the initial size is to be established!

        return rand_num

    @staticmethod
    def get_random_list(data_list, distr, num):
        new_list = []
        trainer = Trainer(data_list)

        # use the specified distribution to get new items
        if distr == 'Pareto':
            new_list = trainer.pareto_multiple_items(num)

        elif distr == 'Gamma':
            new_list = trainer.gamma_multiple_items(num)

        else:
            print("unsupported distribution")

        return new_list

    @staticmethod
    def get_a_single_random_element(data_list, distr):
        new_item = None
        trainer = Trainer(data_list)

        # use the specified distribution to get new items
        if distr == 'Pareto':
            new_item = trainer.pareto_single_item()

        elif distr == 'Gamma':
            new_item = trainer.gamma_single_item()

        else:
            print("unsupported distribution")

        return new_item
