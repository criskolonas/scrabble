from copy import copy
from os.path import exists
from time import strftime
from Player import Player

from Human import Human
from SakClass import SakClass
from itertools import permutations
import json


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
            for i in range(7, 2):
                perms=list(map("".join, permutations(self.hand,i)))
                for perm in perms:
                    for valid in valid_words:
                        if perm.strip() == valid.strip():
                            return perm
        if self.mode == 'smart':
            max_pts=0
            best_word= None
            perms = list(map("".join, permutations(self.hand, i)))
            for perm in perms:
                pts = Game.count_answer_points(perm)
                if pts > max:
                    max = pts
                    best_word = perm

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



    def player_pass(self,player,answer):
        if answer == 'p':
            self.sak.putbackletters(player)
            self.sak.getletters(7,player)
    #plays out a game
    def run(self):
        answer = None
        while answer != 'q' :
            self.sak.getletters(7-len(self.human_1.hand), self.human_1)
            print(repr(self.sak))
            self.show_available_letters(self.human_1)
            answer = self.human_1.play()

            self.player_pass(self.human_1, answer)
            if self.check_given_answer(self.human_1, answer):
                self.human_1.add_score(count_answer_points(answer))
                print(self.human_1.score)
            self.sak.getletters(7-len(self.com_1.hand),self.com_1)
            print(repr(self.sak))
            self.show_available_letters(self.com_1)
            answer_com = self.com_1.play(self.valid_words)
            if answer_com == "none":
                self.player_pass(self.com_1, 'p')
                print(self.com_1.name+" passed !")
            else:
                self.com_1.add_score(count_answer_points(answer_com))
                print(self.com_1.name+" answered "+answer_com+ " and has "+ str(self.com_1.score)+"pts")
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







