class Item:
    """
    This Class contains the mark item method global variable for completing and requiring items.
    Also the init and str methods
    """
    COMPLETED = "c"
    REQUIRED = "r"

    def __init__(self, name, price, priority, required):
        """
        Sets the name, price, priority and required varibale of each item to self.xxxxxx on initialisation
        """
        self.name = name
        self.price = price
        self.priority = priority
        self.required = required

    def __str__(self):
        """
        Overrides the auto string that is set
        """
        return "{} ({}) : ${:2f}".format(self.name, self.price, self.priority)

    def mark_item(self):
        """
        Used to mark item as completed
        """
        self.required = Item.COMPLETED
