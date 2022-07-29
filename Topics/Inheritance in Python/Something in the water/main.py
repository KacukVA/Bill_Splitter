class WaterBody:
    def __init__(self, name, length):
        self.name = name  # str
        self.length = length  # int


class River(WaterBody):
    def flow(self, how: str):
        print(f"{self.name} is flowing {how}!")


lenght = 777
name = 'Seine'
seine = River(name, lenght)
