from game import Game

class Main(object):
    def guidelines(self):
        '''Το παιχνίδι Σκραμπλ. Ο αλγόριθμος του υπολογιστή που χρησιμοποιήθηκε βασίζεται στο σενάριο 1 του pdf.
            -
            Main: κύρια κλάση υπεύθυνη για την εμφάνιση του μενού, την επιλογή ρυθμίσεων και τη δημιουργία αντικειμένου
            τύπου Game για το ξεκίνημα.
            SakClass: κλάση που ειδικεύεται στο σακουλάκι και όλες τις ενέργειες που αφορούν το σακουλακι και τον παίκτη.
            Επίσης περιέχει το dict των γραμμάτων.
            Player: Abstract parent class που κληρωνομούν άνθρωπος και υπολογιστής. Δηλώνεται η μέθοδος play την οποία
            κάνουν override οι απόγονες.
            Human: Κληρωνομεί τα πεδία και κάνει implement την δική της εκδοχή της play
            Computer: Κληρωνομεί τα πεδία και κάνει implement την δική της εκδοχή της play με τον αλγόριθμο του σεναρίου.
            Game: Βασική κλάση υπεύθυνη για την λειτουργία του παιχνιδιού. Παρέχει μεθόδους για το τρεξιμο, τον έλεγχο
            και τα αποτελέσματα μετά το παιχνίδι
            Δομές που χρησιμοποιήθηκαν : Για τα γράμματα,το πλήθος τους και την αξία τους χρησιμοποιήθηκε dictionary όπου
            η μέση πολυπλοκότητα προσπέλασης είναι Ο[1].
            -
            Απαραίτητα αρχεία για τη σωστή λειτουργία είναι:
            main-2959.py
            classes.py
            greek7.txt
            scores.json(έχει ήδη κάποια entries μετά απο testing, τα νέα σκορ θα προστεθούν στο ήδη υπάρχον αρχείο)
        '''

        pass
    def show_menu(self):
        print('***** SCRABBLE ***** \n1:Score\n2:Options\n3:Game\nq:Exit')
    def player_input(self):
        x = input()
        if x == 'q':
            exit()
        elif x == str('1'):
            Game.retrieve_scores()
            Main.show_menu(self)
            Main.player_input(self)
        elif x == str('3'):
            paixnidi = Game('human', 'min')
            paixnidi.run()
        else:
            print('Wrong Input! Try again!')
            Main.show_menu(self)
            Main.player_input(self)


class A:
    def __init__(self):
        print("a")
    def message(self):
        print ("a")

class A2:
    pass
class B(A):
    def message(self):
        print("b")
class C(A2,B):
    pass


if __name__ == '__main__':
    #main = Main()
    #main.show_menu()
    #main.player_input()

    c = C()
    print(in)
    c.message()
