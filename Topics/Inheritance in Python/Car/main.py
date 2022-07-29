class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color


class Tesla(Car):
    def __repr__(self):
        return f'{self.model}, {self.color}'


# create an instance of Tesla
tesla_car = Tesla("3", "black")
