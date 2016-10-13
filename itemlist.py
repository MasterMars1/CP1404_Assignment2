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

    def add_new_item(self, item_name, item_price, item_priority):
        self.items.append([item_name, item_price, item_priority, 'r'])

    def get_item_by_name(self, name):
        for item in self.items:
            if name == item.name:
                return item

    def get_total_price(self, total_price = 0):
        for item in self.items:
            if item.required == 'r':
                total_price += item.price
        return total_price