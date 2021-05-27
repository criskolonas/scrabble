class Letter:
    def __init__(self,character,point):
        self.character= character
        self.point = point

    def __repr__(self):
        return repr(self.character+','+self.point)
