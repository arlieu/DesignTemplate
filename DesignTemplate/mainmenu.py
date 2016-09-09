from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

from kivy.app import App

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
            #self.selectorScreen.inputLabel = newScreen
            self.ids.screenManager.current = 'selectorScreen'
        elif newScreen == 'navigation':
            self.ids.screenManager.current = 'navigationScreen'
        elif newScreen == 'charts':
            self.ids.screenManager.current = 'chartScreen'
        elif newScreen == 'media':
            self.ids.screenManager.current = 'mediaScreen'
        elif newScreen == 'about':
            self.ids.screenManager.current = 'aboutScreen'

    def subMenu1(self, newScreen):
        if self.selectorScreen.ids.selectorScreenManager.current not in self.screenList:
            self.screenList.append(self.selectorScreen.ids.selectorScreenManager.current)

        if newScreen == 'drop down menu':
            self.selectorScreen.ids.selectorScreenManager.current = 'dropdownScreen'
        elif newScreen == 'key pad':
            self.selectorScreen.ids.selectorScreenManager.current = 'keypadScreen'
        elif newScreen == 'checkbox':
            self.selectorScreen.ids.selectorScreenManager.current = 'checkboxScreen'
        elif newScreen == 'sidebar':
            self.selectorScreen.ids.selectorScreenManager.current = 'sidebarScreen'

    def back(self):
        if self.screenList:
            self.ids.screenManager.current = self.screenList.pop()      #  go back to most recent screen
            return True
        return False
        


#class KeyPad(GridLayout):
#    def __init__(self, *args, **kwargs):
#        super(KeyPad, self).__init__(*args, **kwargs)
#        self.cols = 3
#        self.spacing = 10
#        self.createButtons()

#    def createButtons(self):
#        bList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, '', 'Enter']
#        for i in bList:
#            self.add_widget(Button(text=str(i), on_release=self.btnPress))

#    def btnPress(self, btn):
#        # App.get_running_app().root gives instance of app and 
#        # access to MainMenu object
#        selectorScreen = App.get_running_app().root.ids.selectorScreen

#        inputText = selectorScreen.inputBox.text
        