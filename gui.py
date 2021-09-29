from kivy.app import App
from kivy.config import Config
from kivy.config import ConfigParser
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.settings import Settings
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget

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

class CutListOptimizer(App):
    use_kivy_settings = False

    def get_application_config(self):
        return super(CutListOptimizer, self).get_application_config(
            "%(appdir)s/cutlist_settings.ini")

    def build_config(self, config):
        config.setdefaults("OptSection", {
            "opt_type": "Losses",
            "retailer": "None"
        })

    def build(self):
        self.settings_cls = Settings
        return kv_builder

    def on_start(self):
        self.opt_type = self.config.get("OptSection", "opt_type")

    def build_settings(self, settings):
        settings.add_json_panel('Custom', self.config, 'settings_custom.json')

    def on_config_change(self, config, section, key, value):
        if config is self.config:
            token = (section, key)
            if token == ("OptSection", "opt_type"):
                self.opt_type = value

if __name__ == "__main__":
    CutListOptimizer().run()