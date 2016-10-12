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
    status_text = StringProperty()

    def build(self):
        self.items = ItemList()
        items_as_lists = load_items()
        self.items.add_items_from_list(items_as_lists)
        self.title = "Shopping List App"
        self.root = Builder.load_file('app.kv')
        return self.root

    def list_required(self):
        #self.root.ids.bottom_status_text.text = "Click items to mark them as completed"
        self.total_price = 0
        for item in self.items:
            if item.required == 'r':
                self.total_price = self.total_price + item.price
                # create a button for each item
                temp_button = Button(text=item.name)
                temp_button.bind(on_release=self.press_list_required)
                # add the button to the "entriesBox" using add_widget()
                self.root.ids.entry_box.add_widget(temp_button)
        #self.total_price = float(self.total_price)
        #self.root.ids.top_status_text.text = "Total price: ${}".format(self.total_price)

    def list_completed(self):
        self.root.ids.bottom_status_text.text = "Showing completed items"
        self.total_price = 0
        for item in self.items:
            if item.required == 'c':
                # self.total_price = self.total_price + self.item.price
                # create a button for each item
                temp_button = Button(text=item.name)
                temp_button.bind(on_release=self.press_list_completed)
                # add the button to the "entriesBox" using add_widget()
                self.root.ids.entry_box.add_widget(temp_button)
        self.total_price = float(self.total_price)

    def press_list_required(self):
        self.items.mark_item

    def press_list_completed(self):
        self.root.ids.status_text.text = "Showing completed items"

    #def top_status_label(self):
     #   self.root.ids.bottom_status_label.text = str(self.top_status)

    def clear_item_inputs(self):
        self.root.ids.entry_box.clear_widgets()
        self.root.ids.new_item_name.text = ""
        self.root.ids.new_item_price.text = ""
        self.root.ids.new_item_priority.text = ""


Shopping_List_App().run()
