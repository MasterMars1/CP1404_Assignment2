class Item:
    def __init__(self, name, price, priority, required):
        self.name = name
        self.price = price
        self.priority = priority
        self.required = required

    def __str__(self):
        return "{} ({}) : ${:2f}".format(self.name, self.price, self.priority)

    def mark_item(self):
        self.required = "c"