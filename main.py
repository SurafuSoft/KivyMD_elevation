# -*- coding: utf-8 -*-

# import kivy
# kivy.require('1.9.1')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemeManager
from kivymd.navigationdrawer import NavigationDrawer


class KanjiOrigin(App):
    theme_cls = ThemeManager()
    _lastScreen = 'root_screen'
    screen = None
    exit_dialog = None

    def build(self):
        self.title = 'KanjiOrigin'
        main_widget = Builder.load_file('kanjiorigin.kv')
        self.nav_drawer = NavigationDrawer(title="SurafuSoft")
        return main_widget


if __name__ in ('__main__', '__android__'):
    print("App start please")
    KanjiOrigin().run()
