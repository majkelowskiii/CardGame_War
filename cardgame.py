from random import randint

class CardGame(object):


    def create_deck(self):
        deck = []
        figures = ['A']

        for i in range(2, 11):
            figures.append(str(i))

        figures.extend(['J', 'Q', 'K'])

        colors = ['spades', 'diamonds', 'clubs', 'hearts']

        for color in colors:
            for figure in figures:
                deck.append('.'.join((figure,color)))

        return deck


    def name_players(self, players):
        for i in range(0, len(players)):
            print('Wprowadź nazwę gracza', i+1)
            temp = input('> ')
            print(temp)
            print(players[i])
            players[i] = temp
            print(players)


    def split_list_half(self, a_list):

        half = len(a_list)//2
        return a_list[:half], a_list[half:]


    def split_list(self, a_list, no_card_cut):
        return a_list[:no_card_cut], a_list[no_card_cut:]


    def out_faro_shuffle(self, deck):
        # 7-8 farro shuffles in a row == same as the beginning
        deck_to_shuffle = deck
        shuffled_deck = []
        half1, half2 = self.split_list_half(deck_to_shuffle)

        for i in range(0, max(len(half1),len(half2))):
            if half1:
                shuffled_deck.append(half1.pop(0))
            if half2:
                shuffled_deck.append(half2.pop(0))      

        return shuffled_deck  


    def riffle_shuffle(self, deck):

        shuffled_deck = []
        pile1 = []
        pile2 = []

        pile1, pile2 = self.split_list_half(deck)

        while(pile1 or pile2):
            for i in range(0,3):
                if pile1:
                    shuffled_deck.insert(0, pile1.pop())
                else:
                    break

            for i in range(0, 3):        
                if pile2:
                    shuffled_deck.insert(0, pile2.pop())
                else:
                    break    
        
        return shuffled_deck


    def overhand_shuffle(self, deck):

        pre_shuffled_deck = []
        shuffled_deck = []

        while(deck):
            x = min(len(deck), randint(3,9))
            pre_shuffled_deck.insert(0, deck[0:x])
            del deck[0:x]

        for sublist in pre_shuffled_deck:
            for item in sublist:
                shuffled_deck.append(item)

        return shuffled_deck


    def triple_overhand_shuffle(self, deck):
        pass


    def cut_deck(self, deck):

        shuffled_deck = []
        
        cut = randint(1, len(deck)-1)
        half1, half2 = deck[:cut], deck[cut:]
        shuffled_deck = half2 + half1

        return shuffled_deck


    def pile_shuffle(self, deck):

        shuffled_deck = []

        pile1 = []
        pile2 = []
        pile3 = []
        pile4 = []
        pile5 = []
        pile6 = []
        pile7 = []

        while(deck):
            if deck:
                pile1.insert(0, deck.pop(0))
            if deck:
                pile2.insert(0, deck.pop(0))
            if deck:
                pile3.insert(0, deck.pop(0))
            if deck:
                pile4.insert(0, deck.pop(0))
            if deck:
                pile5.insert(0, deck.pop(0))
            if deck:
                pile6.insert(0, deck.pop(0))
            if deck:
                pile7.insert(0, deck.pop(0))

        shuffled_deck = pile7 + pile6 + pile5 + pile4 + pile3 + pile2 + pile1

        return shuffled_deck


    def smooshing(self, deck):
        pass


    def shuffle_deck(self, deck):
        
        shuffled_deck = []
        
        if deck:
            shuffled_deck = self.out_faro_shuffle(deck)
            for i in range(0,2):
                shuffled_deck = self.pile_shuffle(shuffled_deck)

            for i in range(0,8):
                shuffled_deck = self.riffle_shuffle(shuffled_deck)
                shuffled_deck = self.overhand_shuffle(shuffled_deck)

            shuffled_deck = self.cut_deck(shuffled_deck)
        else:
            print("Nothing to shuffle.")


        return shuffled_deck


    def dealcards_2players(self, initial_deck, deck_p1, deck_p2, no_cards=None):

        if no_cards:
            if no_cards > len(initial_deck)//2:
                return 'ERROR'

            for i in range(no_cards):
                deck_p1.insert(0, initial_deck.pop(0))
                deck_p2.insert(0, initial_deck.pop(0))
        else:
            #deal max no. of cards that both players have equal decks
            for i in range(len(initial_deck)//2):
                deck_p1.insert(0, initial_deck.pop(0))
                deck_p2.insert(0, initial_deck.pop(0))
