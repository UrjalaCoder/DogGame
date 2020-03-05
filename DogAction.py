actions = {
    'pee': "Pees on the carpet",
    'rapsu': "Jumps on the bed",
    'hungry': "Eats a carpet"
}

class DogAction:
    def __init__(self, type, value):
        self.type = type if type in actions.keys() else None
        self.value = value
        if self.type is None:
            raise Exception("Invalid dog act!")

    def __str__(self):
        return actions[self.type]
