from kivy.uix.togglebutton import ToggleButton


class CustomToggleButton(ToggleButton):
    def __init__(self, **kwargs):
        super(CustomToggleButton, self).__init__(**kwargs)

        self.group = 'group1'

