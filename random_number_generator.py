import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class RandomNumberApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.min_input = TextInput(hint_text="Min Value", font_size=20, input_filter="int")
        self.max_input = TextInput(hint_text="Max Value", font_size=20, input_filter="int")

        layout.add_widget(self.min_input)
        layout.add_widget(self.max_input)

        generate_btn = Button(text="Generate Random Number", on_press=self.generate, font_size=20)
        layout.add_widget(generate_btn)

        self.result_label = Label(font_size=25)
        layout.add_widget(self.result_label)

        return layout

    def generate(self, instance):
        try:
            min_val = int(self.min_input.text)
            max_val = int(self.max_input.text)
            if min_val >= max_val:
                self.result_label.text = "Min should be less than Max!"
            else:
                random_num = random.randint(min_val, max_val)
                self.result_label.text = f"Generated: {random_num}"
        except ValueError:
            self.result_label.text = "Enter valid numbers!"

if __name__ == "__main__":
    RandomNumberApp().run()
