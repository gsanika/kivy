import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class RPSApp(App):
    def build(self):
        self.choices = ["Rock", "Paper", "Scissors"]
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.result_label = Label(text="Choose Rock, Paper, or Scissors", font_size=20)
        layout.add_widget(self.result_label)

        button_layout = BoxLayout()
        for choice in self.choices:
            btn = Button(text=choice, font_size=20)
            btn.bind(on_press=self.play)
            button_layout.add_widget(btn)

        layout.add_widget(button_layout)

        return layout

    def play(self, instance):
        user_choice = instance.text
        computer_choice = random.choice(self.choices)
        result = self.check_winner(user_choice, computer_choice)
        self.result_label.text = f"You: {user_choice} | Computer: {computer_choice}\n{result}"

    def check_winner(self, user, computer):
        if user == computer:
            return "It's a tie!"
        elif (user == "Rock" and computer == "Scissors") or \
             (user == "Scissors" and computer == "Paper") or \
             (user == "Paper" and computer == "Rock"):
            return "You Win!"
        else:
            return "You Lose!"

if __name__ == "__main__":
    RPSApp().run()
