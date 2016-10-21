from item import Item


class ItemList:
    """
    This class contains all the main function of the shopping list: save items, find items by name, convert list of
    items to a list of object then also back for saving the file, calculate total price, add items and sort items
    by priority.
    """
    def __init__(self):
        """
        Creates self.items list
        """
        self.items = []

    def add_items_from_list(self, items_as_lists):
        """
        Goes through one by one and makes each item from a list to an object. Thus creating a list of objects
        """
        for item in items_as_lists:
            self.items.append(Item(item[0], item[1], item[2], item[3]))

    def __str__(self):
        """
        Overrides the auto string that is set and does it for every item
        """
        for item in self.items:
            return "{}, ${}, priority {}".format(item.name, item.price, item.priority)

    def __iter__(self):
        """
        This is a container method. It allows both iterators and containers too be used with for anf in statements.
        Returns the iterator object itself.
        """
        return iter(self.items)

    def save_items(self):
        """
        Converts the list of objects back into a list of lists for the file writer to write to csv
        """
        ending_items = []
        for item in self.items:
            ending_items.append([item.name, item.price, item.priority, item.required])
        return ending_items

    def get_item_by_name(self, name):
        """
        Goes through self.items and finds the item needed by name
        """
        for item in self.items:
            if name == item.name:
                return item

    def get_total_price(self, total_price=0):
        """
        Goes through self.items and calculates the total price for required items only
        """
        for item in self.items:
            if item.required == Item.REQUIRED:
                total_price += item.price
        return total_price

    def add_item_input(self, name, price, priority):
        """
        Appends the new item to the end of the list
        """
        self.items.append(Item(name, price, priority, "r"))

    def sort_item_by_priority(self):
        """
        Returns self.items after sorting them in order by priority
        """
        self.items.sort(key=lambda item: item.priority)
