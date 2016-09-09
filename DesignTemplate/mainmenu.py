from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty, ObjectProperty

from kivy.uix.screenmanager import Screen

class MainMenu(BoxLayout):
    selectorScreen = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        self.screenList = []

    def changeScreen(self, newScreen):
        # back functionality
        if self.ids.screenManager.current not in self.screenList:
            self.screenList.append(self.ids.screenManager.current)

        # main menu options
        if newScreen == 'selectors':
            self.selectorScreen.inputLabel = newScreen
            self.ids.screenManager.current = 'selectorScreen'
        elif newScreen == 'navigation':
            self.ids.screenManager.current = 'navigationScreen'
        elif newScreen == 'charts':
            self.ids.screenManager.current = 'chartScreen'
        elif newScreen == 'media':
            self.ids.screenManager.current = 'mediaScreen'
        elif newScreen == 'about':
            self.ids.screenManager.current = 'aboutScreen'

    def back(self):
        if self.screenList:
            self.ids.screenManager.current = self.screenList.pop()      #  go back to most recent screen
            return True
        return False


class SelectorScreen(Screen):
    def __init__(self, *args, **kwargs):
        super(SelectorScreen, self).__init__(*args, **kwargs)