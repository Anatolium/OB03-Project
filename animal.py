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
        print(f"{self} ест")

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

# Класс данных всего зоопарка
class Zoo:
    def __init__(self):
        self.animals = []
        self.workers = []

    def add_worker(self, worker):
        self.workers.append(worker)
        print(f"{worker} добавлен в число сотрудников зоопарка")

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal} добавлен в число питомцев зоопарка")

    def show_workers(self):
        print("Сотрудники зоопарка:")
        for worker in self.workers:
            print(worker)
        print()

    def show_animals(self):
        print("Питомцы зоопарка:")
        for animal in self.animals:
            print(animal)
        print()

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


# Функции для демонстрации полиморфизма
def animal_info(animals_list):
    for animal in animals_list:
        animal.get_info()
    print()

def animal_sound(animals_list):
    for animal in animals_list:
        animal.make_sound()
    print()

def animal_eat(animals_list):
    for animal in animals_list:
        animal.eat()
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
animal_eat(animals)

# Создаём объекты классов зоопарка и персонала
zoo = Zoo()
director = ZooDirector("Директор", "Иван Иванович")
keeper = ZooKeeper("Смотритель", "Сергей Сергеевич")
vet = ZooVet("Ветеринар", "Борис Борисович")

# Добавляем сотрудников
zoo.add_worker(director)
zoo.add_worker(keeper)
zoo.add_worker(vet)
print()

# Добавляем животных
zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)
print()

# Выводим состав зоопарка
zoo.show_workers()
zoo.show_animals()

# Специализированные действия сотрудников
staff = [director, keeper, vet]

director.control_zoo()
keeper.feed_animal(animals[0])
vet.heal_animal(animals[1])
