class Worker:
    def __init__(self, name, surname, rate, days):
        self.name = name
        self.surname = surname
        self.rate = rate
        self.days = days

    def salary(self):
        return self.rate * self.days  # Зарплата = ставка × дни


worker1 = Worker("Иван", "Иванович", 2000, 31)

print(f"{worker1.name} {worker1.surname}")
print(f"Зарплата: {worker1.salary()} руб.")