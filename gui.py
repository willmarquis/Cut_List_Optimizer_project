from kivy.app import App
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager

Config.set('graphics', 'window_state', 'maximized')

class MenuWindow(Screen):
     pass

class LinWindow(Screen):
    #def __init__(self, **kwargs): 
        #super(ManualWindow, self).__init__(**kwargs)
    pass

class TwoDWindow(Screen):
    pass

class CutsWindow(Screen):
    pass

class StocksWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv_builder = Builder.load_file("gui.kv")

class Level_US(App):

    def build(self):
        return kv_builder

if __name__ == "__main__":
    Level_US().run()