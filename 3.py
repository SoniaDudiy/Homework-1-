class Automobile:
    def __init__(self, color, model, price):
        self.color = color
        self.model = model
        self.price = price

    def __str__(self):
        return self.model + ": " + self.color + ", " + self.price + "usd."


car1 = Automobile("white", "Bmw", "2 millions ")
car2 = Automobile("black", "Porche", "1 millions ")
car3 = Automobile("grey", "Volkswagen", "2 millions ")
print(car1)
print(car2)
print(car3)