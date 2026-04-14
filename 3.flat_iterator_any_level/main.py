class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.flat_list = []
        self.index = 0

    def flatten(self, items):
        for item in items:
            if isinstance(item, list):
                self.flatten(item)
            else:
                self.flat_list.append(item)

    def __iter__(self):
        self.flat_list = []
        self.index = 0
        self.flatten(self.list_of_list)
        return self

    def __next__(self):
        if self.index >= len(self.flat_list):
            raise StopIteration
        item = self.flat_list[self.index]
        self.index += 1
        return item
