from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App


class KeyPad(GridLayout):
    def __init__(self, *args, **kwargs):
        super(KeyPad, self).__init__(*args, **kwargs)
        self.cols = 13
        self.spacing = 10
        self.textInput = list('')
        self.index = 0
        self.capsPressed = False
        self.shiftPressed = False
        self.createButtons(False, False)

    def createButtons(self, shift, caps):
        self.clear_widgets()
        if shift == True:
           bList = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '<--', \
                'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}', '|', \
                'caps', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '"', 'enter', \
                'shift', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?', 'shift', '']
        elif caps == True:
            bList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '<--', \
                'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}', '\\', \
                'caps', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', "'", 'enter', \
                'shift', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/', 'shift', '']
        else:
             bList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '<--', \
                'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\', \
                'caps', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", 'enter', \
                'shift', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', 'shift', '']


        for i in bList:
            if len(i) > 1:
                self.add_widget(Button(text=str(i), font_size = 12, on_release=self.btnPress))
            else:
                self.add_widget(Button(text=str(i), on_release=self.btnPress))

    def btnPress(self, btn):
        self.index += 1

        if btn.text == '<--':
            if len(self.textInput) > 0:
                self.textInput.pop()
                App.get_running_app().root.ids.selectorScreen.ids.keypadScreen.ids.textBox.text = ''
                for i in range(0, len(self.textInput)):
                    App.get_running_app().root.ids.selectorScreen.ids.keypadScreen.ids.textBox.text += self.textInput[i]
        elif btn.text == 'caps':
            self.shiftPressed = False
            if (self.capsPressed == False):
                self.capsPressed = True
                self.createButtons(False, True) 
            else:
                self.capsPressed = False
                self.createButtons(False, False)
        elif btn.text == 'enter':
            self.textInput.append('\n')
            App.get_running_app().root.ids.selectorScreen.ids.keypadScreen.ids.textBox.text += '\n'
        elif btn.text == 'shift':
            self.capsPressed = False
            if (self.shiftPressed == False):
                self.shiftPressed = True
                self.createButtons(True, False) 
            else:
                self.shiftPressed = False
                self.createButtons(False, False)
        elif btn.text == '':
            App.get_running_app().root.ids.selectorScreen.ids.keypadScreen.ids.textBox.text += ' '
        else:
            self.textInput.append(btn.text)
            App.get_running_app().root.ids.selectorScreen.ids.keypadScreen.ids.textBox.text += btn.text
