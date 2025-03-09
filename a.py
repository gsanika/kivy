from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button

Window.clearcolor = (1, 1, 1, 1)

class MainApp(App):
    def build(self):
        return Button(text="Hello world", font_size="120sp", bold=True, color=(1, 0, 0, 1))

if __name__ == "__main__":
    MainApp().run()
