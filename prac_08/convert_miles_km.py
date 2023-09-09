"""
Kivy example for CP1404/CP5632, IT@JCU
This shows the use of a StringProperty object to store the "model" of MVC
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.6


class MilesConverterApp(App):
    """The class variable in the app is the 'model'."""
    message = StringProperty()

    def build(self):
        """Construct the app."""
        self.title = "Miles to Kilometers Converter"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = "Type in the field & press Enter"
        return self.root

    def handle_calculation(self):
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_number.text = str(result)

    def handle_increment(self, change):
        value = self.get_validated_miles() + change
        self.root.ids.input_number.text = str(value)
        self.handle_calculation()

    def get_validated_miles(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0


MilesConverterApp().run()
