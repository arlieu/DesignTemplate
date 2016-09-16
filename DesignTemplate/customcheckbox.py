from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout


class CustomCheckbox(GridLayout):
    def __init__(self, **kwargs):
        super(GridLayout, self).__init__(**kwargs)

        self.cols = 2
        for i in range(0, 5):
            self.add_widget(CheckBox())