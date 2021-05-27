from copy import copy
from os.path import exists
from time import strftime

from Computer import Computer
from Human import Human
from SakClass import SakClass
from itertools import permutations
import json


class Game:
    def __init__(self,human_name):
        self.valid_words = []
        self.human_name = human_name
        self.human_1 = None
        self.com_1 = None
        self.sak = SakClass()
        self.setup()

    def com_has_move(self):
        return True

    def make_valid_word_list(self):
        with open('greek7.txt','r',encoding="utf8") as f:
            self.valid_words = f.readlines()
    def make_players(self):
        self.human_1 = Human(self.human_name)
        self.com_1 = Computer('Computer')

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

    def check_given_answer(self,player,answer):
        #copy of player's hand
        hand = copy(player.hand)
        #ready to remove used letters if answer is correct
        for char in answer:
            once = False
            for letter in player.hand:
                if char == letter and once == False:
                    hand.remove(letter)
                    once=True
        #creates all string permutations of current hand
        all_perms = list(map("".join, permutations(player.hand)))
        #checks if the answer is a substring of any of the string permutations in hand
        for perm in all_perms:
            if answer in perm:
                #checks if answer exists in valid words
                for word in self.valid_words:
                    if word.strip() == answer.strip():
                        player.hand = copy(hand)
                        print('true')
                        return True
        return False

    def count_answer_points(self,answer):
        counter = 0
        for char in answer:
            counter += self.sak.letter_dict[char][1]
        return  counter

    def player_pass(self,player,answer):
        if answer == 'p':
            self.sak.putbackletters(player)
            self.sak.getletters(7,player)
    #plays out a game
    def run(self):
        answer = None
        while answer != 'q' :
            print(repr(self.sak))

            self.sak.getletters(7-len(self.human_1.hand), self.human_1)
            self.show_available_letters(self.human_1)
            answer = self.human_1.play()
            self.player_pass(self.human_1, answer)
            if self.check_given_answer(self.human_1, answer):
                self.human_1.add_score(self.count_answer_points(answer))
                print(self.human_1.score)

        self.save_scores()





