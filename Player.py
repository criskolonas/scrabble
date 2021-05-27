from abc import ABC,abstractmethod


class Player(ABC):
    def __init__(self,name):
        self.score=0
        self.name = name
        self.hand = []

    @abstractmethod
    def play(self):
        pass

    def add_score(self,pts):
        self.score = self.score + pts