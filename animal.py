# Базовый класс Animal
class Animal:
    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = age
        self.unit = ""

    def __str__(self):
        return f"{self.species} {self.name}"

    def make_sound(self):
        print("** Голос этого животного звучит так:")

    def eat(self):
        print(f"{self.species} {self.name} ест")

    def sleep(self):
        print(f"{self.species} {self.name} спит")

class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__("Птица", name, age)
        self.wing_span = wing_span
        self.unit = "см"

    def get_info(self):
        print(f"{self} имеет размах крыльев {self.wing_span} {self.unit}")

    def make_sound(self):
        super().make_sound()
        print(f"{self} чирикает")

class Mammal(Animal):
    def __init__(self, name, age, running_speed):
        super().__init__("Млекопитающее", name, age)
        self.running_speed = running_speed
        self.unit = "км/ч"

    def get_info(self):
        print(f"{self} бегает со скоростью {self.running_speed} {self.unit}")

    def make_sound(self):
        super().make_sound()
        print(f"{self} издаёт один из характерных звуков млекопитающего")

class Reptile(Animal):
    def __init__(self, name, age, body_temperature):
        super().__init__("Рептилия", name, age)
        self.body_temperature = body_temperature
        self.unit = "°"

    def get_info(self):
        print(f"{self} имеет температуру тела {self.body_temperature}{self.unit}")

    def make_sound(self):
        super().make_sound()
        print(f"{self} шипит")

# Базовый класс сотрудников зоопарка
class ZooStaff:
    def __init__(self, profession,  name):
        self.profession = profession
        self.name = name

    def __str__(self):
        return f"{self.profession} {self.name}"

class ZooDirector(ZooStaff):
    def control_zoo(self):
        print(f"{self} руководит зоопарком")

class ZooKeeper(ZooStaff):
    def feed_animal(self, animal):
        print(f"{self} кормит питомца {animal}")

class ZooVet(ZooStaff):
    def heal_animal(self, animal):
        print(f"{self} лечит питомца {animal.species} {animal.name}")

# Класс данных всего зоопарка
class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal} добавлен в число питомцев зоопарка")

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"{employee} добавлен в число сотрудников зоопарка")

    def show_animals(self):
        print("Питомцы зоопарка:")
        for animal in self.animals:
            print(animal)
        print()

    def show_employees(self):
        print("Сотрудники зоопарка:")
        for employee in self.employees:
            print(employee)
        print()

# Функции для демонстрации полиморфизма
def animal_info(animals_list):
    for animal in animals_list:
        animal.get_info()
    print()

def animal_sound(animals_list):
    for animal in animals_list:
        animal.make_sound()
    print()


# ---------------------------------------- Тест --------------------------------------------------

# Создаём объекты животных
bird = Bird("Павлин", 3, 150)
mammal = Mammal("Пантера", 5, 80)
reptile = Reptile("Питон", 2, 30)

# Создаём список животных и демонстрируем полиморфизм
animals = [bird, mammal, reptile]
animal_info(animals)
animal_sound(animals)

# Создаём объекты классов
zoo = Zoo()
director = ZooDirector("Директор", "Иван Иванович")
keeper = ZooKeeper("Смотритель", "Сергей Сергеевич")
vet = ZooVet("Ветеринар", "Борис Борисович")

# Добавляем сотрудников и животных в зоопарк
zoo.add_employee(director)
zoo.add_employee(keeper)
zoo.add_employee(vet)
print()

zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)
print()

# Выводим состав зоопарка
zoo.show_employees()
zoo.show_animals()

# Специализированные действия сотрудников
staff = [director, keeper, vet]

director.control_zoo()
keeper.feed_animal(animals[0])
vet.heal_animal(animals[1])
