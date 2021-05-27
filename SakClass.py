from random import shuffle


class SakClass:
    letter_dict = {'Α': [12, 1], 'Β': [1, 8], 'Γ': [2, 4], 'Δ': [2, 4], 'Ε': [8, 1],
                   'Ζ': [1, 10], 'Η': [7, 1], 'Θ': [1, 10], 'Ι': [8, 1], 'Κ': [4, 2],
                   'Λ': [3, 3], 'Μ': [3, 3], 'Ν': [6, 1], 'Ξ': [1, 10], 'Ο': [9, 1],
                   'Π': [4, 2], 'Ρ': [5, 2], 'Σ': [7, 1], 'Τ': [8, 1], 'Υ': [4, 2],
                   'Φ': [1, 8], 'Χ': [1, 8], 'Ψ': [1, 10], 'Ω': [3, 3]}
    def __init__(self):
        self.sak = []
        self.make_sak()

    def __repr__(self):
        return repr('Στο σακουλάκι γράμματα:' + str(len(self.sak)))

    #calls random.shuffle to shuffle letters in the sak
    def randomize_sak(self):
        shuffle(self.sak)

    #adds all the letters and their duplicates in a list
    def make_sak(self):
        for letter in self.letter_dict:
            for i in range(self.letter_dict[letter][0]):
                self.sak.append(letter)


    def putbackletters(self,player):
        for letter in player.hand:
            self.sak.append(letter)
        player.hand.clear()

    def getletters(self,n,player):
        if len(self.sak) >= n:
            self.randomize_sak()
            for i in range(n):
                player.hand.append(self.sak.pop())

