from kivy.app import App
from kivy.core.window import Window

import webbrowser

from mainmenu import MainMenu


class DesignTemplateApp(App):
    def __init__(self, **kwargs):
        super(DesignTemplateApp, self).__init__(**kwargs)
        Window.bind(on_keyboard=self.back)

    def back(self, window, key, *args):
        if key == 27:   # esc = back
            return self.root.back()     #  runs back method in MainMenu

    def build(self):
        return MainMenu()

    def getText(self):
        return ('This app demos different UI designs\n'
                'and components that may be used for\n'
                'future projects')

    def on_ref_press(self, instance, ref): 
        links = {
            'link1': 'https://github.com/arlieu',
            'link2': 'https://www.linkedin.com/in/avery-lieu-541344110?authType=NAME_SEARCH&authToken=Rl8c&locale=en_US&trk=tyah&trkInfo=clickedVertical%3Amynetwork%2CclickedEntityId%3A466650625%2CauthType%3ANAME_SEARCH%2Cidx%3A1-1-1%2CtarId%3A1473376757190%2Ctas%3Aavery'
            }

        webbrowser.open(links[ref])     #  opens link on default browser