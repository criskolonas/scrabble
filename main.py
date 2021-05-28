import self as self

from Game import Game


class Main(object):
    @staticmethod
    def show_menu(self):
        print('***** SCRABBLE ***** \n1:Score\n2:Options\n3:Game\nq:Exit')
    @staticmethod
    def player_input(self):
        x = input()
        if x == 'q':
            exit()
        elif x == str('1'):
            Game.retrieve_scores()
            Main.show_menu(self)
            Main.player_input(self)
        elif x == str('3'):
            paixnidi = Game('human','min')
            paixnidi.run()
        else:
            print('Wrong Input! Try again!')
            Main.show_menu(self)
            Main.player_input(self)

if __name__ == '__main__':
    Main.show_menu(self)
    Main.player_input(self)


