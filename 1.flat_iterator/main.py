class FlatIterator:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists
        self.outer_index = 0
        self.inner_index = 0

    def __iter__(self):
        self.outer_index = 0
        self.inner_index = 0
        return self

    def __next__(self):
        while self.outer_index < len(self.list_of_lists):
            if self.inner_index < len(self.list_of_lists[self.outer_index]):
                item = self.list_of_lists[self.outer_index][self.inner_index]
                self.inner_index += 1
                return item
            self.outer_index += 1
            self.inner_index = 0
        raise StopIteration
