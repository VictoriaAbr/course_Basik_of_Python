from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, n):
        self.n = n

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        return self.consumption + other.consumption


class Coat(Clothes):

    @property
    def consumption(self):
        return (self.n / 6.5) + 0.5


class Suit(Clothes):

    @property
    def consumption(self):
        return ((self.n * 2) + 0.3) / 100


coat = Coat(42)
print(coat.consumption)
suit = Suit(170)
print(suit.consumption)

print(coat + suit)

