from DogAction import DogAction

"""
This class describes a Dog.
"""

# Different breeds.
DogBreeds = [
    'Cairin Terrieri',
    'Cockerspanieli',
    'Lapin koira AKA Aurum',
    'Corgi',
    'Tuomas'
]

class Dog:
    def __init__(self, name, breed, initialAge = 0):
        self.name = name
        self.breed = breed if (breed in DogBreeds) else None
        self.age = initialAge
        self.hunger = 0
        self.needToPee = 0
        self.needToBeRapsutus = 0
        if self.breed is None:
            raise Exception("Invalid dog breed.")

    def update(self):
        self.hunger += 1
        self.needToPee += 1
        self.needToBeRapsutus += 1

    def feed(self):
        self.hunger = 0

    def rapsuttaa(self):
        self.needToBeRapsutus = 0

    def walking(self):
        self.needToPee = 0

    def act(self):
        newActs = []
        if self.needToPee > 5:
            self.needToPee = 0
            act = DogAction('pee', 3)
            newActs.append(act)
        if self.needToBeRapsutus > 2:
            act = DogAction('rapsu', 1)
            newActs.append(act)
        if self.hunger > 4:
            act = DogAction('hungry', 2)
            newActs.append(act)
        return newActs

    def grow(self):
        self.age += 1

    def __str__(self):
        return f"{self.name} : {self.breed}"
