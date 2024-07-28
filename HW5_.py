import random

count=0

food = int(input('Введите начальное количество еды: '))

class AnimalSpecies:
    def __init__(self,name,size,foodtype,area,lifespan):
        self.name=name
        self.size=size
        self.foodtype=foodtype
        self.area=area
        self.lifespan=lifespan

    def info(self):
        return (f'Вид: {self.name}, размер (кг): {self.size}, питание: {self.foodtype}, среда обитания: {self.area}, срок жизни: {self.lifespan}')
    
species = [
    AnimalSpecies('Окунь', 2, 'травоядное', 'вода', 10),
    AnimalSpecies('Сом', 30, 'травоядное', 'вода', 25),
    AnimalSpecies('Карп', 20, 'травоядное', 'вода', 20),
    AnimalSpecies('Щука', 15, 'хищник', 'вода', 15),
    AnimalSpecies('Орел', 5, 'хищник', 'воздух', 20),
    AnimalSpecies('Голубь', 0.5, 'травоядное', 'воздух', 5),
    AnimalSpecies('Скворец', 0.1, 'травоядное', 'воздух', 4),
    AnimalSpecies('Воробей', 0.05, 'травоядное', 'воздух', 5),
    AnimalSpecies('Кабан', 100, 'травоядное', 'земля', 15),
    AnimalSpecies('Газель', 45, 'травоядное', 'земля', 12),
    AnimalSpecies('Овечька', 80, 'травоядное', 'земля', 15),
    AnimalSpecies('Лев', 200, 'хищник', 'земля', 15)
]

class Animal:
    def __init__(self, species, age = 0, satiety = 50, gender = None):
        self.species = species
        self.age = age
        self.satiety = satiety
        self.gender = gender

    def info(self):
        return (f'Вид: {self.species.name}, возраст: {self.age}, сытость: {self.satiety}, пол: {self.gender}')
    
    def age_animal(self):
        self.age += 1

    def increase_satiety(self,num):
        self.satiety = min(100, self.satiety + num)

    def decrease_satiety(self,num):
        self.satiety = max(0, self.satiety - num)

    def starved(self):
        return self.satiety < 10
    
    def dead(self):
        return self.age >= self.species.lifespan
    
class Planet:
    def __init__(self):
        self.food = food
        self.population = []

    def create(self, species, gender=None):
        if gender is None:
            gender = 'муж' if random.randint(0,1) == 0 else 'жен'
        new_animal = Animal(species, age = 0, satiety = 50,gender = gender)
        self.population.append(new_animal)

    def info_population(self):
        for i in self.population:
            print(i.info())

    def breed_animals(self, parent1, parent2):
        if parent1.species != parent2.species:
            return
        
        if parent1.gender == parent2.gender:
            return


        if parent1.species.area == 'вода' and parent1.satiety > 50:
            for _ in range(10):
                gender = 'муж' if random.randint(0,1) == 0 else 'жен'
                self.population.append(Animal(parent1.species, satiety=23, gender=gender))
        elif parent1.species.area == 'воздух' and parent1.satiety > 42 and parent1.age > 3:
            for _ in range(4):
                gender = 'муж' if random.randint(0,1) == 0 else 'жен'
                self.population.append(Animal(parent1.species, satiety=64, gender=gender))
        elif parent1.species.area == 'земля' and parent1.satiety > 20 and parent1.age > 5:
            for _ in range(2):
                gender = 'муж' if random.randint(0,1) == 0 else 'жен'
                self.population.append(Animal(parent1.species, satiety=73, gender=gender))

    def time_step(self):
        new_population = []

        for animal in self.population:
            animal.age_animal()

            if animal.dead():
                self.food += animal.species.size
                continue
            
            if animal.species.foodtype == 'травоядное':
                if self.food > 0:
                    self.food -= 1
                    animal.increase_satiety(26)
                else:
                    animal.decrease_satiety(9)
            else:
                if random.random() < 0.5:
                    animal.increase_satiety(53)
                else:
                    animal.decrease_satiety(16)
                
            if not animal.starved():
                new_population.append(animal)
            else:
                self.food += animal.species.size

        self.population = new_population

        self.population = [animal for animal in self.population if not animal.starved()]

        print(f"Осталось еды: {self.food}")
        self.info_population()

planet = Planet()

print('Доступные виды: ')
for i,sp in enumerate(species):
    print(f'{i+1}.{sp.info()}')

for i,sp in enumerate(species):
    choice = int(input(f'Введите количество особей вида {species[i].name}: '))
    select = species[i]
    for _ in range(choice):
        planet.create(select)

planet.info_population()

time=int(input('Введите временной отрезок: '))

for _ in range(time):
    print("\nTime step:")
    planet.time_step()

    if len(planet.population) > 1:
        pairs = set()
        while len(pairs) < len(planet.population) // 2:
            parent1, parent2 = random.sample(planet.population, 2)
            if (parent1, parent2) not in pairs and (parent2, parent1) not in pairs:
                pairs.add((parent1, parent2))
        for parent1, parent2 in pairs:
            planet.breed_animals(parent1, parent2)