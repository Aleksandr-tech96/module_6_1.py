# Родительский класс "Животное"
class Animal:
    alive = True # живой
    fed = False # накормленный
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

# Дочерний класс "Млекопитающее" родительского класса "Животное"
class Mammal(Animal):
    pass

# Дочерний класс "Хищник" родительского класса "Животное"
class Predator(Animal):
    pass

# Родительский класс "Растение"
class Plant:
    edible = False # съедобность
    def __init__(self, name):
        self.name = name

# Дочерний класс "Цветок" родительского класса "Растение"
class Flower(Plant):
    pass

# Дочерний класс "Фрукты" родительского класса "Растение"
class Fruit(Plant):
    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')

p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)

print(a1.alive)
print(a2.fed)