from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from itemlist import ItemList
from item import Item
from HarmonSinghA1 import load_items
import csv

__author__ = 'Harmon Singh'


class Shopping_List_App(App):
    top_status_label = StringProperty()
    bottom_status_label = StringProperty()

    def build(self):
        self.items = ItemList()
        items_as_lists = load_items()
        self.items.add_items_from_list(items_as_lists)
        self.title = "Shopping List App"
        self.root = Builder.load_file('app.kv')
        self.list_required()
        return self.root

    def list_required(self):
        self.bottom_status_text.text = "Click items to mark them as completed"
        for item in self.items:
            if item.required == 'r':
                if item.priority == 1:
                    temp_button = Button(background_color=[1, 0, 0, 1], text=item.name)
                elif item.priority == 2:
                    temp_button = Button(background_color=[0, 1, 0, 1], text=item.name)
                elif item.priority == 3:
                    temp_button = Button(background_color=[0, 0, 1, 1], text=item.name)
                # create a button for each item
                temp_button.bind(on_release=self.mark_item)
                temp_button.bind(on_release=self.bottom_status_label)
                # add the button to the "entriesBox" using add_widget()
                self.root.ids.entry_box.add_widget(temp_button)
        self.total_price = float(self.total_price)
        self.root.ids.top_status_text.text = "Total price: ${}".format(self.total_price)

    def list_completed(self):
        #self.root.ids.bottom_status_text.text = "Showing completed items"
        for item in self.items:
            if item.required == 'c':
                # create a button for each item
                temp_button = Button(text=item.name)
                temp_button.bind(on_release=self.press_list_completed)
                # add the button to the "entriesBox" using add_widget()
                self.root.ids.entry_box.add_widget(temp_button)
        #self.total_price = float(self.total_price)

    def mark_item(self, instance):
        name = instance.text
        item = self.items.get_item_by_name(name)
        item.mark_item()
        self.clear_all()
        self.list_required()

    def press_list_completed(self):
        self.root.ids.status_text.text = "Showing completed items"

    def bottom_status_label(self):
        self.bottom_status_label.text = self.bottom_status

    def top_status_label(self):
        self.top_status_label.text = self.top_status

    def clear_all(self):
        self.root.ids.entry_box.clear_widgets()
        self.root.ids.new_item_name.text = ""
        self.root.ids.new_item_price.text = ""
        self.root.ids.new_item_priority.text = ""

    def new_item_name(self):
        name = self.root.ids.new_item_name.text
        return name

    def new_item_price(self):
        price = self.root.ids.new_item_price.text
        return price

    def new_item_priority(self):
        priority = self.root.ids.new_item_priority.text
        return priority

    def add_item(self):
        self.items.add_new_item(self.new_item_name(), self.new_item_price(), self.new_item_priority())


Shopping_List_App().run()
