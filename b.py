from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        btn = Button(text="Click Me!", font_size=25)

        def on_button_click(instance):
            btn.text = "Clicked!"

        btn.bind(on_press=on_button_click)
        return btn

if __name__ == "__main__":
    MyApp().run()
