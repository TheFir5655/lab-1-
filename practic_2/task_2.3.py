class Numbers:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Числа: {self.x} и {self.y}")

    def change(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def sum(self):
        return self.x + self.y

    def max(self):
        return self.x if self.x > self.y else self.y


nums = Numbers(3, 5)
nums.show()
nums.change(8, 2)
nums.show()
print("Сумма:", nums.sum())
print("Большее:", nums.max())