class Fruit:
    def __init__(self, color, taste):
        self.color = color
        self.taste = taste

class Mango(Fruit):
    def __init__(self, color, taste, variety):
        super().__init__(color, taste)
        self.variety = variety
        self.color = "yellowish green"  


mango = Mango("yellow", "sweet", "Alphonso")
print("Mango - Color:", mango.color, ", Taste:", mango.taste, ", Variety:", mango.variety)
