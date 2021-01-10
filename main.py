from kivymd.app import MDApp
from views.rootlay import RootLay

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Light"
        return RootLay()


MainApp().run()