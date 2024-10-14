class Fruit:
    def __init__(self, color, taste):
        self.color = color
        self.taste = taste

class Mango(Fruit):
    def __init__(self, color, taste, variety):
        super().__init__(color, taste)
        self.variety = variety

class Apple(Fruit):
    def __init__(self, color, taste, origin):
        super().__init__(color, taste)
        self.origin = origin

class Orange(Fruit):
    def __init__(self, color, taste, vitamin_c):
        super().__init__(color, taste)
        self.vitamin_c = vitamin_c

class Grapes(Fruit):
    def __init__(self, color, taste, seedless):
        super().__init__(color, taste)
        self.seedless = seedless


mango = Mango("yellow", "sweet", "Alphonso")
print("Mango - Color:", mango.color, ", Taste:", mango.taste, ", Variety:", mango.variety)

apple = Apple("red", "sweet and tart", "Washington")
print("Apple - Color:", apple.color, ", Taste:", apple.taste, ", Origin:", apple.origin)

orange = Orange("orange", "tangy", "high")
print("Orange - Color:", orange.color, ", Taste:", orange.taste, ", Vitamin C content:", orange.vitamin_c)

grapes = Grapes("purple", "sweet", True)
print("Grapes - Color:", grapes.color, ", Taste:", grapes.taste, ", Seedless:", grapes.seedless)
