from Player import Player


class Human(Player):
    def __init__(self,name):
        super(Human,self).__init__(name)

    def play(self):
        answer = input('Λέξη:')
        return answer
