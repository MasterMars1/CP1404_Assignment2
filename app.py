from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from itemlist import ItemList
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

    # Load items from csv and put in a list called item_list
    # def load_items(self):
    #     self.item_list = []
    #     with open('items.csv', 'r', newline='') as file:
    #         for item in file.readlines():
    #             item = item.strip().split(',')
    #             item[2] = int(item[2])
    #             item[1] = float(item[1])
    #             self.item_list.append(item)
    #         self.item_list.sort(key=lambda row: row[2], reverse=False)
    #     return self.item_list

    # Write list item_list back on the csv file after alterations
    # def write_items(item_list):
    #     with open("items.csv", 'w', newline='') as file:
    #         writer = csv.writer(file)
    #         for item in item_list:
    #             writer.writerow(item)

    def list_required(self):
        self.total_price = 0
        for item in self.items:
            if item.required == 'r':
                self.item.price = self.total_price + self.item.price
                # create a button for each item
                temp_button = Button(text=item.name)
                temp_button.bind(on_release=self.press_list_required)
                # add the button to the "entriesBox" using add_widget()
                self.root.ids.entry_box.add_widget(temp_button)
        #return self.total_price

    def list_completed(self):
        self.total_price = 0
        for item in self.items:
            if item.required == 'c':
                self.item.price = self.total_price + self.item.price
                # create a button for each item
                temp_button = Button(text=item.name)
                temp_button.bind(on_release=self.press_list_completed)
                # add the button to the "entriesBox" using add_widget()
                self.root.ids.entry_box.add_widget(temp_button)
        self.total_price = float(self.total_price)

    def press_list_required(self):
        #Mark item as completed
        self.status_text = "Click items to mark them as completed"

    def press_list_completed(self):
        #Mark item as required
        self.status_text = "These are the items that have been completed"

    def total_cost_label(self, total_cost):
        self.root.ids.total_cost_label.text = "Total price: ${}".format(self.total_cost)


Shopping_List_App().run()
