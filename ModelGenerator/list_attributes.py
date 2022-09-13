from numpy import random

from ModelGenerator.Trainer import Trainer


class ListAttribute:
    number_of_items: int = 0
    item_size_list: [int] = []
    item_intervals_list: [int] = []

    def __init__(self, number_of_items=0, item_size_list=None, item_intervals_list=None):
        self.number_of_items = number_of_items
        self.item_size_list = item_size_list
        self.item_intervals_list = item_intervals_list
        if number_of_items == 0 or self.item_intervals_list is None or self.item_size_list is None:
            self.number_of_items = 0
            self.item_size_list = []
            self.item_intervals_list = []

    def train_list(self, size_distr, interval_distr):
        random_number = self.get_random_the_number_of_items()

        new_sizes = self.get_random_list(self.item_size_list, size_distr, random_number)
        new_intervals = self.get_random_list(self.item_intervals_list, interval_distr, (random_number - 1))

        return random_number, new_sizes, new_intervals

    def get_random_the_number_of_items(self):
        rand_num = 0

        # todo use the specified distribution to get a random number
        rand_num = int(random.normal(loc=self.number_of_items, scale=3.0, size=None))
        assert isinstance(rand_num, int), 'Random number - wrong type!'

        if rand_num < 0:
            rand_num *= -1

        # todo know if rand_num == 0 the initial size is to be established!

        return rand_num

    @staticmethod
    def get_random_list(data_list, distr, num):
        new_list = []
        trainer = Trainer(data_list)

        # todo use the specified distribution to get new items
        if distr == 'Pareto':
            new_list = trainer.pareto(num)

        elif distr == 'Gamma':
            new_list = trainer.gamma(num)

        else:
            print("unsupported distribution")

        return new_list
