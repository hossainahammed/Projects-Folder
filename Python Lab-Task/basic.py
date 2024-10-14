class Bird:
    def __init__(self, species, color, can_fly):
        self.species = species
        self.color = color
        self.can_fly = can_fly

    def fly(self):
        if self.can_fly:
            return f"The {self.color} {self.species} is flying."
        else:
            return f"The {self.color} {self.species} cannot fly."

    def sing(self):
        return f"The {self.color} {self.species} is singing."



bird1 = Bird("Robin", "red", True)
bird2 = Bird("Parrot", "green", True)
bird3 = Bird("Penguin", "black and white", False)
bird4 = Bird("Eagle", "brown", True)
bird5 = Bird("Canary", "yellow", True)


print(bird1.fly())
print(bird2.sing())
print(bird3.fly())
print(bird4.fly())
print(bird5.sing())
