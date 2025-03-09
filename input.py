from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import BoxLayout

class MyApp(MDApp):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        self.username = MDTextField(hint_text="Enter your name")
        btn = MDRaisedButton(text="Submit", pos_hint={"center_x": 0.5})

        def on_submit(instance):
            print("Hello,", self.username.text)

        btn.bind(on_press=on_submit)
        layout.add_widget(self.username)
        layout.add_widget(btn)
        return layout

if __name__ == "__main__":
    MyApp().run()
