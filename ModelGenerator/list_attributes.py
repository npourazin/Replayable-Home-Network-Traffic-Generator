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

    def train_list(self):
        pass
