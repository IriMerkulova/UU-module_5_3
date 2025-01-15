# Задача "Нужно больше этажей":
class House:
        def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for floor in range(1, new_floor + 1):
                print(floor)


    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other
        else:
            return False
    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other
        else:
            return NotImplemented
    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors <= other
        else:
            return NotImplemented
    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors > other
        else:
            return NotImplemented
    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors >= other
        else:
            return NotImplemented
    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors != other
        else:
            return True

    def __add__(self, value):
        if isinstance(value, House):
            self.number_of_floors = self.number_of_floors + value.number_of_floors
            return self
        elif isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
            return self
        else:
            NotImplemented
    def __radd__(self, value):
        return House(self.name, self.number_of_floors + value)
    def __iadd__(self, value):
        if isinstance(value, House):
            self.number_of_floors += value.number_of_floors
            return self
        elif isinstance(value, int):
            self.number_of_floors += value
            return self
        else:
            NotImplemented
    def __sub__(self, value):
        if isinstance(value, House):
            self.number_of_floors -= value.number_of_floors
            return self
        elif isinstance(value, int):
            self.number_of_floors -= value
            return self
        else:
            NotImplemented
    def __isub__(self, value):
        if isinstance(value, House):
            self.number_of_floors -= value.number_of_floors
            return self
        elif isinstance(value, int):
            self.number_of_floors -= value
            return self
        else:
            NotImplemented

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)


print(h1)
print(h2)
print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)

print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__

print(h1 >= h2) # __ge__

print(h1 < h2) # __lt__

print(h1 <= h2) # __le__

print(h1 != h2) # __ne__

h1 = h1 - 1 # __sub__
print(h1)
h2 -= 1 # __isub__
print(h2)

