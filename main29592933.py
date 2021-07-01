from classes import Game


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
            Για την μέθοδο play υλοποιήθηκαν οι αλγόριθμοιτου σεναρίου 1 και 2.
              - Min - Max - Smart (ΑΕΜ: 2959): 
              - Smart - Fail (ΑΕΜ: 2933): Χρησιμοποιήθηκε διαφορετικό implementation του smart από ότι στο παραπάνω σενάριο.
              Ο fail αρχικά υπολογίζει τον μέσο όρο από τα βάρη των διαθέσιμων permutations ανά γύρο, και αφαιρεί τις λέξεις
              με βάρος μικρότερο από το μέσο, με τη βοήθεια της λίστας target_keys. Έπειτα, αφού αποθηκεύσει τα βάρη των λέξεων
              που μείνανε, με την βοήθεια της built-in συνάρτησης choices της βιβλιοθήκης random, "διαλέγει", ανάλογα με το βάρος
              της κάθε λέξης και τον παράγοντα της τύχης, μια λέξη για να παίξει ο υπολογιστής, χωρίς αυτή πάντα να είναι η καλύτερη
              διαθέσιμη, προσομοιώνοντας κάπως καλύτερα τον παράγοντα του ανθρώπινου λάθους στην επιλογή του.
            Game: Βασική κλάση υπεύθυνη για την λειτουργία του παιχνιδιού. Παρέχει μεθόδους για το τρεξιμο, τον έλεγχο
            και τα αποτελέσματα μετά το παιχνίδι
            Δομές που χρησιμοποιήθηκαν : Για το λεξικό, τα γράμματα,το πλήθος τους και την αξία τους χρησιμοποιήθηκε
            dictionary, όπου η μέση πολυπλοκότητα προσπέλασης είναι Ο[1].
            -
            Απαραίτητα αρχεία για τη σωστή λειτουργία είναι:
            main29592933.py
            classes.py
            greek7.txt
            scores.json(έχει ήδη κάποια entries μετά απο testing, τα νέα σκορ θα προστεθούν στο ήδη υπάρχον αρχείο)
        '''

        pass

    def show_menu(self):
        print('***** SCRABBLE ***** \n1:Score\n2:Options\n3:Game\nq:Exit')

    def player_input(self):
        x = input()
        gamemode = 'min'
        if x == 'q':
            exit()
        elif x == str('1'):
            Game.retrieve_scores()
            Main.show_menu(self)
            Main.player_input(self)
        elif x == str('2'):
            inp = input("Επέλεξε τρόπο παιχνιδιού υπολογιστή!\n1.Min(Default)\n2.Max\n3.Smart\n4.Smart-Fail\n")
            if inp == str('1'):
                gamemode = 'min'
            elif inp == str('2'):
                gamemode = 'max'
            elif inp == str('3'):
                gamemode = 'smart'
            elif inp == str('4'):
                gamemode = 'smart-fail'
            else:
                print("Λάθος input! Το default είναι το min")
            print("Παιχνίδι σε {} mode".format(gamemode))
            paixnidi = Game('human', gamemode)
            paixnidi.run()

        elif x == str('3'):
            paixnidi = Game('human', gamemode)
            paixnidi.run()
        else:
            print('Wrong Input! Try again!')
            Main.show_menu(self)
            Main.player_input(self)


if __name__ == '__main__':
    main = Main()
    main.show_menu()
    main.player_input()
