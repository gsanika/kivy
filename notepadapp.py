from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class NotepadApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.text_input = TextInput(font_size=20, multiline=True)
        layout.add_widget(self.text_input)

        btn_layout = BoxLayout()
        save_btn = Button(text="Save", on_press=self.save_text, font_size=20)
        load_btn = Button(text="Load", on_press=self.load_text, font_size=20)

        btn_layout.add_widget(save_btn)
        btn_layout.add_widget(load_btn)
        layout.add_widget(btn_layout)

        return layout

    def save_text(self, instance):
        with open("notes.txt", "w") as f:
            f.write(self.text_input.text)

    def load_text(self, instance):
        try:
            with open("notes.txt", "r") as f:
                self.text_input.text = f.read()
        except FileNotFoundError:
            self.text_input.text = "No saved notes!"

if __name__ == "__main__":
    NotepadApp().run()
