from item import Item


class ItemList:
    def __init__(self):
        self.items = []

    def add_items_from_list(self, items_as_lists):
        for item in items_as_lists:
            self.items.append(Item(item[0], item[1], item[2], item[3]))

    def __str__(self):
        for item in self.items:
            return "{}, ${}, priority {}".format(item.name, item.price, item.priority)

    def __iter__(self):
        return iter(self.items)
