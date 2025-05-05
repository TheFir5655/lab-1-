class Calculation:
    def __init__(self):
        self.line = ""

    def set_line(self, value):
        self.line = value

    def add_symbol(self, symbol):
        self.line += symbol

    def get_line(self):
        return self.line

    def get_last(self):
        return self.line[-1] if self.line else ""

    def delete_last(self):
        if self.line:
            self.line = self.line[:-1]

c = Calculation()
c.set_line("2+2")
print(c.get_line())

c.add_symbol("*3")
print(c.get_line())

print(c.get_last())

c.delete_last()
print(c.get_line())