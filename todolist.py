from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class ToDoApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.input_task = TextInput(hint_text="Enter task", font_size=20)
        self.layout.add_widget(self.input_task)

        add_button = Button(text="Add Task", font_size=20, on_press=self.add_task)
        self.layout.add_widget(add_button)

        self.tasks_layout = BoxLayout(orientation='vertical')
        self.layout.add_widget(self.tasks_layout)

        return self.layout

    def add_task(self, instance):
        task_text = self.input_task.text
        if task_text:
            task_label = Label(text=task_text, font_size=18)
            self.tasks_layout.add_widget(task_label)
            self.input_task.text = ""

if __name__ == "__main__":
    ToDoApp().run()
