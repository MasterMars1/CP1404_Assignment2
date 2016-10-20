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
    This Class is the main program. Methods are called from other classes to provide the kivy with tasks for buttons labels etc.
    """
    top_status_label = StringProperty()
    bottom_status_label = StringProperty()

    def build(self):
        """
        Builds the GUI using kivy and performs tasks on boot
        """
        self.items = ItemList()
        items_as_lists = load_items()
        self.items.add_items_from_list(items_as_lists)
        self.title = "Shopping List App"
        self.root = Builder.load_file('app.kv')
        self.list_required()
        return self.root

    def list_required(self):
        """
        Lists required items by creating widgets for marking off items and giving them colour based on priority. This is also sorted by priority and keeps the list required button highlighter after press.
        """
        self.items.sort_item_by_priority()
        self.clear_all()
        self.root.ids.list_required.state = "down"
        self.root.ids.list_completed.state = "normal"
        self.bottom_status_label = "Click items to mark them as completed"
        for item in self.items.items:
            if item.required == Item.REQUIRED:
                temp_button = Button(text=item.name, background_color=BUTTON_COLOURS[item.priority])
                # create a button for each item
                temp_button.bind(on_release=self.mark_item)
                # add the button to the "entriesBox" using add_widget()
                self.root.ids.entry_box.add_widget(temp_button)
        total_price = self.items.get_total_price()
        self.top_status_label = "Total price: ${}".format(total_price)

    def list_completed(self):
        """
        Lists completed items by creating widgets for completed items. Also keeps the list completed button highlighted after press.
        """
        self.root.ids.list_required.state = "normal"
        self.root.ids.list_completed.state = "down"
        self.bottom_status_label = "Showing completed items"
        for item in self.items.items:
            if item.required == Item.COMPLETED:
                # create a button for each item
                temp_button = Button(text=item.name)
                temp_button.bind(on_release=self.display_item_info)
                # add the button to the "entriesBox" using add_widget()
                self.root.ids.entry_box.add_widget(temp_button)

    def mark_item(self, instance):
        name = instance.text
        item = self.items.get_item_by_name(name)
        item.mark_item()
        self.clear_all()
        self.list_required()

    def display_item_info(self, instance):
        name = instance.text
        item = self.items.get_item_by_name(name)
        self.bottom_status_label = "{}, ${}, priority {} (completed)".format(item.name, item.price, item.priority)

    def clear_all(self):
        self.root.ids.entry_box.clear_widgets()
        self.root.ids.new_item_name.text = ""
        self.root.ids.new_item_price.text = ""
        self.root.ids.new_item_priority.text = ""
        self.top_status_label = ""
        self.bottom_status_label = ""

    def new_item_name(self):
        name = self.root.ids.new_item_name.text
        self.invalid_name = True
        while self.invalid_name:
            if name.replace(" ", "") == "":
                self.bottom_status_label = "All fields must be completed"
            else:
                self.invalid_name = False
        return name

    def new_item_price(self):
        self.invalid_price = True
        while self.invalid_price:
            try:
                price = self.root.ids.new_item_price.text
                if price < 0:
                    self.bottom_status_label = "Price must not be negative"
                    continue
            except ValueError:
                self.bottom_status_label = "Please enter a valid number"
            else:
                self.invalid_price = False
        return price

    def new_item_priority(self):
        self.invalid_priority = True
        while self.invalid_priority:
            try:
                priority = self.root.ids.new_item_priority.text
                if priority < 1 or priority > 3:
                    self.bottom_status_label = "Priority must be 1, 2 or 3"
                    continue
            except ValueError:
                self.bottom_status_label = "Please enter a valid number"
            else:
                self.invalid_priority = False
        return priority

    def add_item(self):
        new_item = Item(self.new_item_name(), self.new_item_price(), self.new_item_priority(), Item.REQUIRED)
        if self.invalid_name == False and self.invalid_price == False and self.invalid_priority == False:
            self.items.add_new_item(new_item)
            self.root.ids.new_item_name.text = ""
            self.root.ids.new_item_price.text = ""
            self.root.ids.new_item_priority.text = ""
            self.list_required()

    def on_stop(self):
        write_items(self.items.get_items_as_list())


ShoppingListApp().run()
