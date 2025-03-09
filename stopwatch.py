from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock

class StopwatchApp(App):
    def build(self):
        self.time = 0
        self.running = False

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.label = Label(text="0.0", font_size=50)
        layout.add_widget(self.label)

        btn_layout = BoxLayout()

        start_btn = Button(text="Start", on_press=self.start, font_size=20)
        stop_btn = Button(text="Stop", on_press=self.stop, font_size=20)
        reset_btn = Button(text="Reset", on_press=self.reset, font_size=20)

        btn_layout.add_widget(start_btn)
        btn_layout.add_widget(stop_btn)
        btn_layout.add_widget(reset_btn)
        layout.add_widget(btn_layout)

        return layout

    def update(self, dt):
        if self.running:
            self.time += dt
            self.label.text = f"{self.time:.1f}"

    def start(self, instance):
        if not self.running:
            self.running = True
            Clock.schedule_interval(self.update, 0.1)

    def stop(self, instance):
        self.running = False

    def reset(self, instance):
        self.time = 0
        self.label.text = "0.0"
        self.running = False

if __name__ == "__main__":
    StopwatchApp().run()
