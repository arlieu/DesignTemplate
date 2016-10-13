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
        self.screenList = []    #  Order of visited screens for 'back' 
        self.mainMenu = set(['startScreen', 'selectorScreen', 'navigationScreen', \
            'chartScreen', 'mediaScreen', 'aboutScreen'])    
        self.selectorMenu = set(['selectorStartScreen', 'buttonScreen', \
            'togglebuttonScreen', 'checkboxScreen', 'keypadScreen'])   
        self.navigatorMenu = set(['navigationStartScreen', 'dropdownScreen', \
            'sidebarScreen', 'menubarScreen', 'searchboxScreen']) 

    def changeScreen(self, newScreen):
        # back functionality
        if self.ids.screenManager.current not in self.screenList:
            self.screenList.append(self.ids.screenManager.current)

        # main menu options
        if newScreen == 'selectors':
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

        if newScreen == 'button':
            self.ids.selectorScreen.selectorScreenManager.current = 'buttonScreen'
        elif newScreen == 'toggle button':
            self.ids.selectorScreen.selectorScreenManager.current = 'togglebuttonScreen'
        elif newScreen == 'checkbox':
            self.ids.selectorScreen.selectorScreenManager.current = 'checkboxScreen'
        elif newScreen == 'key pad':
            self.ids.selectorScreen.selectorScreenManager.current = 'keypadScreen'

    def subMenu2(self, newScreen):
        if self.ids.navigationScreen.navigationScreenManager.current not in self.screenList:
            self.screenList.append(self.ids.navigationScreen.navigationScreenManager.current)

        if newScreen == 'drop down':
            self.ids.navigationScreen.navigationScreenManager.current = 'dropdownScreen'
        elif newScreen == 'sidebar':
            self.ids.navigationScreen.navigationScreenManager.current = 'sidebarScreen'
        elif newScreen == 'menu bar':
            self.ids.navigationScreen.navigationScreenManager.current = 'menubarScreen'
        elif newScreen == 'search box':
            self.ids.navigationScreen.navigationScreenManager.current = 'searchboxScreen'

    def back(self):
        if self.screenList:
            tmp = self.screenList.pop()
            if tmp in self.mainMenu:
                self.ids.screenManager.current = tmp      #  go back to most recent screen
            elif tmp in self.selectorMenu:
                self.ids.selectorScreen.selectorScreenManager.current = tmp
            elif tmp in self.navigatorMenu:
                self.ids.navigationScreen.navigationScreenManager.current = tmp
            return True
        return False