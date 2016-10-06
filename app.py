from kivy.app import App
from kivy.lang import Builder

class Shopping_List_App(App):
    def build(self):
        self.title = "Shopping List App"
        self.root = Builder.load_file('app.kv')
        return self.root