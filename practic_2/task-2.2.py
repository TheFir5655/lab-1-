class Train:
    def __init__(self, destination, number, time):
        self.destination = destination
        self.number = number
        self.time = time

    def __str__(self):
        return f"Поезд #{self.number} в {self.destination}, отправление {self.time}"


trains = [
    Train("Москва", "da11", "08:45"),
    Train("Алаяска", "123", "12:30"),
    Train("Крым", "bd12", "15:15")
]

num = input("Введите номер поезда: ")
found = [t for t in trains if t.number == num]
print(found[0] if found else "Поезд не найден")