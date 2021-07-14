#!python3

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang.builder import Builder
import re

class CalculatorWidget(Widget):
    def clear(self):
        self.ids.input_box.text = "0"

    def number_press(self, number):
        prev_number = self.ids.input_box.text
        if number == "0":
            if prev_number == "0":
                pass
            else:
                self.ids.input_box.text = prev_number + number
            
        if prev_number == "0":
            self.ids.input_box.text = ""
            self.ids.input_box.text = str(number)
        else:
            self.ids.input_box.text = prev_number + number

    def sign_button_press(self):
        prev_number = self.ids.input_box.text
        if prev_number[0] == "-":
            self.ids.input_box.text = prev_number[1:]
        else:
            self.ids.input_box.text = "-" + prev_number

    def dot_button_press(self):
        numbers = re.split("[\+\-*/]", self.ids.input_box.text)
        if "." in numbers[-1]:
            pass
        else:
            self.ids.input_box.text += "."

    def delete_button_press(self):
        if len(self.ids.input_box.text) > 1:
            self.ids.input_box.text = self.ids.input_box.text[:-1] 
        else:
            self.ids.input_box.text = "0"

    def divide_button_press(self):
        prev_number = self.ids.input_box.text
        self.clear()

    def arithmetic_button_press(self, sign):
        self.ids.input_box.text += sign

    def equal_button_press(self):
        self.ids.input_box.text = str(eval(self.ids.input_box.text))

class CalculatorApp(App):
    def build(self):
        return CalculatorWidget()

def main():
    Builder.load_file("./calculatorWithKivy.kv")
    Window.size = (850, 550)
    CalculatorApp().run()

if __name__ == "__main__":
    main()
