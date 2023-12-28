from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import wikipedia
import urllib.request

Builder.load_string("""
<FirstScreen>:
    GridLayout:
        cols: 1
        padding: 10
        spacing: 10
        Image:
            id: img
            size_hint_y: 0.8
        TextInput:
            id: user_query
            size_hint_y: 0.1
        Button:
            text: 'Search Image'
            size_hint_y: 0.1
            on_press: root.search_image()

<RootWidget>:
    FirstScreen:
        id: first_screen
        name: 'first_screen'
""")

# Each new screen will require separate class
class FirstScreen(Screen):

    def search_image(self):
        query = self.manager.current_screen.ids.user_query.text
        page = wikipedia.page(query)
        image_link = page.images[0] # This will force the app to choose the first photo found from query input.
        urllib.request.urlretrieve(image_link, 'query_image.jpg')
        self.manager.current_screen.ids.img.source = 'query_image.jpg'


class RootWidget(ScreenManager):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()

MainApp().run()