from kivy.uix.dropdown import DropDown


class CustomDropDown(DropDown):
    def __init__(self, *args, **kwargs):
        super(CustomDropDown, self).__init__(*args, **kwargs)

        for i in range(5):
            btn = Button(text='Option %d' % i, size_hint_y=None, height=40)
            btn.bind(on_release=lambda btn:self.select(btn.text))
            self.add_widget(btn)

        mainbutton = Button(text='Drop Down', size_hint=(None, None))
        mainbutton.bind(on_release=self.open)
        self.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
        self.add_widget(mainbutton)