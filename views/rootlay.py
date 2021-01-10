import os

from kivy.lang import Builder

from kivy.uix.floatlayout import FloatLayout

class RootLay(FloatLayout):
    pass

Builder.load_file(os.path.join(os.path.dirname(__file__), "./rootlay.kv"))