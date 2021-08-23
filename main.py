from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import os

# fix opengl error
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

Builder.load_file('frontend.kv')


class FirstScreen(Screen):
    def search_image(self):
        pass


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
