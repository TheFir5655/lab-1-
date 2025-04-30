class Counter:
    def __init__(self, start=0):
        self.value = start

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def get_current(self):
        return self.value


counter1 = Counter()
print(counter1.get_current())

counter1.increment()
counter1.increment()
print(counter1.get_current())
counter1.decrement()
print(counter1.get_current())

counter2 = Counter(5)
print(counter2.get_current())