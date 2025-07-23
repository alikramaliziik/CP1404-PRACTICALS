"""
CP1404 prac8 Workshop - GUI program to convert miles to kilometres

"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window



MILES_TO_KM = 1.60934

class MilesConverterApp(App):
    """ MilesConverterApp is a Kivy App for converting miles to kilometres """
    output_text = StringProperty("0.0")

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (300, 150)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation, output result to label widget """
        try:
            miles = float(value) if value else 0
            result = miles * MILES_TO_KM
            self.output_text = str(round(result, 5))
        except ValueError:
            self.output_text = "0.0"

    def handle_increment(self, change):
        """ handle up/down button press, update the text input with new value """
        try:
            value = float(self.root.ids.input_miles.text) if self.root.ids.input_miles.text else 0
            new_value = max(0, value + change)
            self.root.ids.input_miles.text = str(new_value)
            self.handle_calculate(new_value)
        except ValueError:
            self.root.ids.input_miles.text = str(max(0, change))
            self.handle_calculate(max(0, change))

MilesConverterApp().run()
