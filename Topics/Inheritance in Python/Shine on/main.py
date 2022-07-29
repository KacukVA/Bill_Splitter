class Star:
    def __init__(self, name, spectral_class):
        self.name = name
        self.spectral_class = spectral_class

class YellowDwarf(Star):
    def __str__(self):
        return f'{self.name}, is inherited from class Star'
