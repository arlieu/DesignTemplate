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
        self.createButtons()

    def createButtons(self):
        bList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'backspace', \
            'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\', \
            '', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", 'enter', \
            '', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', 'shift', 'CLEAR']
        for i in bList:
            if i == '':
                self.add_widget(Label(text=''))
            else:
                if len(i) > 1:
                    self.add_widget(Button(text=str(i), font_size= min(self.height, self.width)/10, on_release=self.btnPress))
                else:
                    self.add_widget(Button(text=str(i), on_release=self.btnPress))

    def btnPress(self, btn):
        self.index += 1

        if btn.text == 'backspace':
            if len(self.textInput) > 0:
                self.textInput.pop()
                App.get_running_app().root.ids.selectorScreen.ids.keypadScreen.ids.textBox.text = ''
                for i in range(0, len(self.textInput)):
                    App.get_running_app().root.ids.selectorScreen.ids.keypadScreen.ids.textBox.text += self.textInput[i]
        elif btn.text == 'enter':
            self.textInput.append('\n')
            App.get_running_app().root.ids.selectorScreen.ids.keypadScreen.ids.textBox.text += '\n'
        elif btn.text == 'shift':
            pass 
        elif btn.text.lower() == 'clear':
            self.textInput = []
            App.get_running_app().root.ids.selectorScreen.ids.keypadScreen.ids.textBox.text = ''
        else:
            self.textInput.append(btn.text)
            App.get_running_app().root.ids.selectorScreen.ids.keypadScreen.ids.textBox.text += btn.text
