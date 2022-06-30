class car:
    def __init__(self, *args, **kwargs):
        self.wheels = 4
        self.windows = 4
        self.color = kwargs.get("color", "black")
        self.mupler = kwargs.get("mupler", 1)

    def start(self):
        print(f"I Started")

    def __str__(self):
        return f"{self.wheels} car!!"


class convertible(car):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.time = kwargs.get("time", 10)

    def __str__(self):
        return f"{self.time} take for convertiblity"


porche = car(color="red", mupler="2")
print(porche.color)

mini = car()
print(mini.color)

conv = convertible(time=30, color="yellow", mupler="4")
print(conv)
print(conv.color)
