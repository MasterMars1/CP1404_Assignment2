class Item:
    COMPLETED = "c"
    REQUIRED = "r"

    def __init__(self, name, price, priority, required):
        self.name = name
        self.price = float(price)
        self.priority = int(priority)
        self.required = required

    def __str__(self):
        return "{} ({}) : ${:2f}".format(self.name, self.price, self.priority)

    def mark_item(self):
        self.required = Item.COMPLETED
