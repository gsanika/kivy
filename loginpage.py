from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class LoginApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.username = TextInput(hint_text="Username", font_size=20)
        self.password = TextInput(hint_text="Password", font_size=20, password=True)

        login_btn = Button(text="Login", font_size=20, on_press=self.check_login)
        self.result_label = Label(font_size=18)

        layout.add_widget(self.username)
        layout.add_widget(self.password)
        layout.add_widget(login_btn)
        layout.add_widget(self.result_label)

        return layout

    def check_login(self, instance):
        if self.username.text == "admin" and self.password.text == "1234":
            self.result_label.text = "Login Successful!"
        else:
            self.result_label.text = "Invalid Credentials"

if __name__ == "__main__":
    LoginApp().run()
