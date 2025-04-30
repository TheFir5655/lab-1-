class SimpleClass:
    def __init__(self, x=10, y=20):
        self.x = x
        self.y = y
        print(f"Создан объект со значениями: {x} и {y}")

    def __del__(self):
        print(f"Удален объект со значениями: {self.x} и {self.y}")

print("Создание объекта с параметрами:")
obj1 = SimpleClass(5, 15)

print("Создание объекта по умолчанию:")
obj2 = SimpleClass()

print("Удаление объектов:")
del obj1
del obj2