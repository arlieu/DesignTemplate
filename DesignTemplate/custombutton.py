from kivy.uix.button import Button


class CustomButton(Button):
    def __init__(self, **kwargs):
        super(CustomButton, self).__init__(**kwargs)

        self.text = 'Press Button'
        self.bind(on_press=self.callback)

    def callback(instance, value):
        if instance.text == 'Button Pressed':
            instance.text = 'Press Button'
            instance.background_color = (0.0, 1.0, 0.0, 1.0)
        else:
            instance.text = 'Button Pressed'
            instance.background_color = (1.0, 0.0, 0.0, 1.0)



