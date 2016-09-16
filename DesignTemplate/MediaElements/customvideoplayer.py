from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.gridlayout import GridLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup


class CustomVideoPlayer(VideoPlayer):
    def __init__(self, **kwargs):
        super(CustomVideoPlayer, self).__init__(**kwargs)

        #content = Button(text='Still in development...')
        #popup = Popup(title='Video Demo', content=content)
        #content.bind(on_press=popup.dismiss)
        #popup.open()

        self.source = 'http://80.250.191.10:1935/live/hlsstream343/playlist.m3u8'
        self.state = 'pause'
        self.options = {
            'allow_stretch': True
            }

    def playType(self, choice):
        if choice == 'livestream':
            self.source = 'http://80.250.191.10:1935/live/hlsstream343/playlist.m3u8'
        elif choice == 'stream':
            self.source = ''
        else: 
            self.source =''

