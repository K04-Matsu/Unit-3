from kivymd.app import MDApp
from kivy.core.window import Window

Window.size = (473, 700)

class calculator(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.first_input = 0
        self.second_input = 0
        self.operator = ""

    def zero(self):
        if self.root.ids.num.text == "0":
            self.root.ids.num.text = "0"
        elif self.root.ids.num.text != "0":
            self.root.ids.num.text += "0"
    def one(self):
        if self.root.ids.num.text == "0":
            self.root.ids.num.text = "1"
        elif self.root.ids.num.text != "0":
            self.root.ids.num.text += "1"
    def two(self):
        if self.root.ids.num.text == "0":
            self.root.ids.num.text = "2"
        elif self.root.ids.num.text != "0":
            self.root.ids.num.text += "2"
    def three(self):
        if self.root.ids.num.text == "0":
            self.root.ids.num.text = "3"
        elif self.root.ids.num.text != "0":
            self.root.ids.num.text += "3"
    def four(self):
        if self.root.ids.num.text == "0":
            self.root.ids.num.text = "4"
        elif self.root.ids.num.text != "0":
            self.root.ids.num.text += "4"
    def five(self):
        if self.root.ids.num.text == "0":
            self.root.ids.num.text = "5"
        elif self.root.ids.num.text != "0":
            self.root.ids.num.text += "5"
    def six(self):
        if self.root.ids.num.text == "0":
            self.root.ids.num.text = "6"
        elif self.root.ids.num.text != "0":
            self.root.ids.num.text += "6"
    def seven(self):
        if self.root.ids.num.text == "0":
            self.root.ids.num.text = "7"
        elif self.root.ids.num.text != "0":
            self.root.ids.num.text += "7"
    def eight(self):
        if self.root.ids.num.text == "0":
            self.root.ids.num.text = "8"
        elif self.root.ids.num.text != "0":
            self.root.ids.num.text += "8"
    def nine(self):
        if self.root.ids.num.text == "0":
            self.root.ids.num.text = "9"
        elif self.root.ids.num.text != "0":
            self.root.ids.num.text += "9"

    def add(self):
        self.root.ids.num.text += "+"
    def sub(self):
        self.root.ids.num.text += "-"
    def mul(self):
        self.root.ids.num.text += "*"
    def div(self):
        self.root.ids.num.text += "/"

    def neg(self):
        self.root.ids.num.text = "-" + self.root.ids.num.text
    def dec(self):
        if self.root.ids.num.text[-1] not in "+-*÷":
            self.root.ids.num.text += "."
    def per(self):
        if "+-*÷" not in self.root.ids.num.text:
            temp = float(self.root.ids.num.text)
            self.root.ids.num.text = str(temp / 100)

    def equal(self):
        self.root.ids.num.text = str(round(eval(self.root.ids.num.text), 7))
    def clear(self):
        self.first_input = 0
        self.second_input = 0
        self.root.ids.num.text = "0"

    def build(self):
        return


calculator = calculator()
calculator.run()
