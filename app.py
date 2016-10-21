from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from itemlist import ItemList
from item import Item
from HarmonSinghA1 import load_items
from HarmonSinghA1 import write_items

"""
Name: Harmon Singh
Date: 21/10/16
Brief Description: This program will effectively perform the actions of a shopping list. Allow the user to add
                   a new item, look at required items, look at completed items and mark an item as completed.
GitHub URL: https://github.com/hamsingh/CP1404_Assignment2.git
"""

__author__ = 'Harmon Singh'
BUTTON_COLOURS = {1: (1, 0, 0, 1), 2: (0, 1, 0, 1), 3: (0, 0, 1, 1)}


class ShoppingListApp(App):
    """
    This Class is the main program. Methods are called from other classes to provide
    the kivy with tasks for buttons labels etc.
    """
    top_status_label = StringProperty()
    bottom_status_label = StringProperty()

    def build(self):
        """
        Builds the GUI using kivy and performs tasks on boot. Loads items as a list of lists, into items as lists
        """
        self.items = ItemList()
        items_as_lists = load_items()
        self.items.add_items_from_list(items_as_lists)
        self.title = "Shopping List App"
        self.root = Builder.load_file('app.kv')
        self.list_required()
        return self.root

    def on_stop(self):
        """
        Writes self.items to csv by calling the method save_items in itemlist.py
        """
        items = self.items.save_items()
        write_items(items)

    def list_required(self):
        """
        Lists required items by creating widgets for marking off items and giving them colour based on priority.
        This is also sorted by priority and keeps the list required button highlighter after press.
        """
        self.items.sort_item_by_priority()
        self.root.ids.entry_box.clear_widgets()
        self.root.ids.list_required.state = "down"
        self.root.ids.list_completed.state = "normal"
        self.bottom_status_label = "Click items to mark them as completed"
        for item in self.items.items:
            if item.required == Item.REQUIRED:
                temp_button = Button(text=item.name, background_color=BUTTON_COLOURS[item.priority])
                # create a button for each item
                temp_button.bind(on_release=self.mark_item)
                # add the button to the "entry_box" using add_widget()
                self.root.ids.entry_box.add_widget(temp_button)
        total_price = self.items.get_total_price()
        self.top_status_label = "Total price: ${}".format(total_price)

    def list_completed(self):
        """
        Lists completed items by creating widgets for completed items.
        Also keeps the list completed button highlighted after press.
        """
        self.root.ids.entry_box.clear_widgets()
        self.root.ids.list_required.state = "normal"
        self.root.ids.list_completed.state = "down"
        self.bottom_status_label = "Showing completed items"
        for item in self.items.items:
            if item.required == Item.COMPLETED:
                # create a button for each item
                temp_button = Button(text=item.name)
                temp_button.bind(on_release=self.display_item_info)
                # add the button to the "entry_box" using add_widget()
                self.root.ids.entry_box.add_widget(temp_button)

    def mark_item(self, instance):
        """
        Marks the item clicked on as completed
        """
        name = instance.text
        item = self.items.get_item_by_name(name)
        item.mark_item()
        self.clear_all()
        self.list_required()

    def display_item_info(self, instance):
        """
        Displays the items information in the bottom status label (at the bottom of the app)
        """
        name = instance.text
        item = self.items.get_item_by_name(name)
        self.bottom_status_label = "{}, ${}, priority {} (completed)".format(item.name, item.price, item.priority)

    def clear_new_item_inputs(self):
        """
        Clears the input boxes that ask for item name, pirce and priority
        """
        self.root.ids.new_item_name.text = ""
        self.root.ids.new_item_price.text = ""
        self.root.ids.new_item_priority.text = ""

    def get_new_item(self):
        """
        Gets the inputs from the text input boxes and runs them through error checking before calling the add new item
        method in itemlist.py and then resets the list required to include the new item
        """
        name = self.root.ids.new_item_name.text
        price = self.root.ids.new_item_price.text
        priority = self.root.ids.new_item_priority.text

        if name == "" or price == "" or priority == "":
            self.bottom_status_label = "All fields must be completed"
        else:
            try:
                price = float(price)
                # The error checking enables the user to correctly input and any incorrect inputs is dealt by displaying
                # an error
                if price < 0:
                    self.bottom_status_label = "Price must not be negative"
                    return
            except ValueError:
                self.bottom_status_label = "Please enter a valid number"
                return

            try:
                priority = int(priority)
                if priority <= 0 or priority > 3:
                    self.bottom_status_label = "Priority must be 1, 2 or 3"
                    return
            except ValueError:
                self.bottom_status_label = "Please enter a valid number"
                return

            # this is the method from itemlist that appends the new item to the existing list
            self.items.add_item_input(name, price, priority)
            self.list_required()
            self.clear_new_item_inputs()


ShoppingListApp().run()
