class Item:
    def __init__(self, name="", price=0, priority=1):
        self.name = name
        self.price = price
        self.priority = priority

    def __str__(self):
        return "{} ({}) : ${:2f}".format(self.name, self.price, self.priority)

    def __float__(self):
        float = 3