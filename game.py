from copy import copy
from os.path import exists
from time import strftime
from random import shuffle
from abc import ABC,abstractmethod
from itertools import permutations
import json



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

class Computer(Player) :
    def __init__(self,name,mode):
        super(Computer,self).__init__(name)
        self.mode = mode

    def play(self,valid_words):
        if self.mode == 'min':
            for i in range(2, 7):
                perms=list(map("".join, permutations(self.hand,i)))
                for perm in perms:
                    for valid in valid_words:
                        if perm.strip() == valid.strip():
                            return perm
        if self.mode == 'max':
            for i in reversed(range(2, 7)):
                perms=list(map("".join, permutations(self.hand,i)))
                print(perms)
                for perm in perms:
                    for valid in valid_words:
                        if perm.strip() == valid.strip():
                            return perm
        if self.mode == 'smart':

            max_pts=0
            best_word= None
            for i in range(2,7):
                perms = list(map("".join, permutations(self.hand, i)))
                for valid in valid_words:
                    for perm in perms:
                        if perm.strip() == valid.strip():
                            pts = Game.count_answer_points(perm)
                            if pts > max_pts:
                                max_pts = pts
                                best_word = perm
            if best_word is not None:
                return best_word
        return "none"



class Game:
    valid_words = []



    def __init__(self,human_name,mode):
        self.human_name = human_name
        self.human_1 = None
        self.com_1 = None
        self.mode = mode
        self.sak = SakClass()
        self.setup()

    def com_has_move(self):
        return True

    def make_valid_word_list(self):
        with open('greek7.txt','r',encoding="utf8") as f:
            self.valid_words = f.readlines()
    def make_players(self):
        self.human_1 = Human(self.human_name)
        self.com_1 = Computer('Computer',self.mode)

    def setup(self):
        self.make_valid_word_list()
        self.make_players()

    def show_available_letters(self,player):
        print(player.name+' Διαθέσιμα Γράμματα:',end='')
        for letter in player.hand:
            print('['+letter+','+str(self.sak.letter_dict[letter][1])+']',end='')

    def save_scores(self):
        if not exists("scores.json"):
            open("scores.json",'x')

        with open("scores.json", 'r+') as outf:
            match_score = {
                'Human:': self.human_1.score,
                'Computer': self.com_1.score
            }
            data = json.load(outf)
            data[strftime("%d/%m/%Y %H:%M:%S")] =match_score
            outf.seek(0)
            json.dump(data, outf)

    def remove_used_letters(self,player,answer):
        hand = copy(player.hand)
        # ready to remove used letters if answer is correct
        for char in answer:
            once = False
            for letter in player.hand:
                if char == letter and once == False:
                    hand.remove(letter)
                    once = True
        player.hand = copy(hand)

    def check_given_answer(self,player,answer):

        #creates all string permutations of current hand
        all_perms = list(map("".join, permutations(player.hand)))
        #checks if the answer is a substring of any of the string permutations in hand
        for perm in all_perms:
            if answer in perm:
                #checks if answer exists in valid words
                for word in self.valid_words:
                    if word.strip() == answer.strip():
                        return True
        return False



    def player_pass(self,player,answer):
        if answer == 'p':
            self.sak.putbackletters(player)
            self.sak.getletters(7,player)
    #plays out a game
    def run(self):
        answer = None
        while answer != 'q' :
            #Human
            self.sak.getletters(7-len(self.human_1.hand), self.human_1)
            print(repr(self.sak))
            self.show_available_letters(self.human_1)
            answer = self.human_1.play()
            self.player_pass(self.human_1, answer)
            if self.check_given_answer(self.human_1, answer):
                pts = self.count_answer_points(answer)
                self.human_1.add_score(pts)
                self.remove_used_letters(self.human_1,answer)
                print('Αποδεκτή Λέξη:'+answer+' Πόντοι:'+str(pts)+' Σύνολο:'+str(self.human_1.score))
            input('Enter για συνεχεια')
            #Computer
            self.sak.getletters(7-len(self.com_1.hand),self.com_1)
            print(repr(self.sak))
            self.show_available_letters(self.com_1)
            answer_com = self.com_1.play(self.valid_words)
            if answer_com == "none":
                self.player_pass(self.com_1, 'p')
                print(self.com_1.name+" passed !")
            else:
                pts_com = self.count_answer_points(answer_com)
                self.com_1.add_score(pts_com)
                print(self.com_1.name+" answered "+answer_com+ " and has "+ str(self.com_1.score)+"pts")
                self.remove_used_letters(self.com_1,answer_com)
                print('Αποδεκτή Λέξη:'+answer_com+' Πόντοι:'+str(pts_com)+' Σύνολο:'+str(self.com_1.score))

                self.sak.getletters(7 - len(self.com_1.hand), self.com_1)

        self.save_scores()

    @classmethod
    def retrieve_scores(cls):
        with open("scores.json", 'r') as outf:
            data = json.load(outf)
            for game in data:
                print(game)
                print(data[game])

    @classmethod
    def count_answer_points(cls, answer):
        counter = 0
        for char in answer:
            counter += SakClass.letter_dict[char][1]
        return counter


class Human(Player):
    def __init__(self,name):
        super(Human,self).__init__(name)

    def play(self):
        answer = input('Λέξη:')
        return answer





