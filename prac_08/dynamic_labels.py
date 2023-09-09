from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    status_text = StringProperty()

    def build(self):
        self.title = "Dynamic Labels app"
        self.root = Builder.load_file('dynamic_labels.kv')
        name_labels = ["Alice", "Bob", "Charlie", "David", "Eve"]

        for name in name_labels:
            temp_button = Label(text=name)
            self.root.ids.entries_label.add_widget(temp_button)

        return self.root


DynamicLabelsApp().run()
