class Student:
    def __init__(self, surname, date, grades, group):
        self.surname = surname
        self.date = date
        self.grades = grades
        self.group = group

    def __str__(self):
        return f"\nСтудент: {self.surname}\nДата: {self.date}\nГруппа: {self.group}\nОценки: {self.grades}"


students = [
    Student("Иван", "15.10.2006", [2, 5, 2, 5, 1, 4], "101"),
    Student("Игорь", "25.07.2007", [2, 5, 2, 5, 1, 4], "101"),
    Student("Иннокентий", "12.05.2006", [2, 5, 2, 5, 1, 4], "101"),
    Student("Игнатий", "04.02.2006", [2, 5, 2, 5, 1, 4], "101"),
    Student("Ирина", "23.12.2006", [2, 5, 2, 5, 1, 4], "101"),
    Student("Ирина", "14.05.2006", [2, 5, 2, 5, 1, 4], "101"),
    Student("Илья", "01.01.2007", [2, 5, 2, 5, 1, 4], "101")
]


def show_students():
    print("\n".join(f"{i + 1}. {s.surname}" for i, s in enumerate(students)))


def modify_student():
    show_students()
    try:
        choice = int(input("\nНомер студента: ")) - 1
        if 0 <= choice < len(students):
            student = students[choice]
            print(student)
            action = input("\n1-Фамилия\n2-Дата\n3-Группа\n4-Назад\nВыбор: ")
            if action == "1":
                student.surname = input("Новая фамилия: ")
            elif action == "2":
                student.date = input("Новая дата: ")
            elif action == "3":
                student.group = input("Новая группа: ")
            elif action == "4":
                return
            else:
                print("Неверный ввод!")
        else:
            print("Неверный номер!")
    except:
        print("Ошибка ввода!")


while True:
    choice = input("\n1-Список\n2-Изменить\n3-Выход\nВыбор: ")
    if choice == "1":
        print("\n".join(str(s) for s in students))
    elif choice == "2":
        modify_student()
    elif choice == "3":
        break
    else:
        print("Неверный ввод!")