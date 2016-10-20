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

    def add_new_item(self, item):
        self.items.append(item)

    def get_item_by_name(self, name):
        for item in self.items:
            if name == item.name:
                return item

    def get_total_price(self, total_price=0):
        for item in self.items:
            if item.required == Item.REQUIRED:
                total_price += item.price
        return total_price

    def get_items_as_list(self):
        return [[item.name, item.price, item.priority, item.required] for item in self.items]

    def sort_item_by_priority(self):
        sorted(self.items, key=lambda item: item.priority)
