
class Animal:
    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        self._age = age  # Encapsulated attribute
        self.sound = sound

    def make_sound(self):
        return f"{self.name} the {self.species} says {self.sound}!"

    def get_age(self):
        return self._age

    def celebrate_birthday(self):
        self._age += 1
        return f"{self.name} is now {self._age} years old."

# Subclass: Lion


class Lion(Animal):
    def __init__(self, name, age, pride_name):
        super().__init__(name, "Lion", age, "Roar")
        self.pride_name = pride_name

    def hunt(self):
        return f"{self.name} is hunting with the {self.pride_name} pride."

# Subclass: Elephant


class Elephant(Animal):
    def __init__(self, name, age, tusk_length):
        super().__init__(name, "Elephant", age, "Trumpet")
        self.tusk_length = tusk_length

    def spray_water(self):
        return f"{self.name} sprays water with its trunk!"

# Polymorphism Example


def animal_show(animal):
    print(animal.make_sound())
    print(animal.celebrate_birthday())


# Testing the classes
simba = Lion("Simba", 5, "River Pride")
dumbo = Elephant("Dumbo", 10, 1.5)

animal_show(simba)
print(simba.hunt())

print()

animal_show(dumbo)
print(dumbo.spray_water())
