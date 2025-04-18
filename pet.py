class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5 #initial hunger level
        self.energy = 5 #initial energy level
        self.happiness = 1 #initial happiness level
        self.tricks = []  # List to keep tricks

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} ate some food! 🍖")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} had a nice nap! 😴")

    def play(self):
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} played happily! 🐾")

    def get_status(self):
        print(f"🐶 {self.name}'s Status:")
        print(f"   Hunger: {self.hunger}/10")
        print(f"   Energy: {self.energy}/10")
        print(f"   Happiness: {self.happiness}/10")

    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick}! 🎉")

    def show_tricks(self):
        print(f"{self.name} knows these tricks:")
        for trick in self.tricks:
            print(f" - {trick}")
