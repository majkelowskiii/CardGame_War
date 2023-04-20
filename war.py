from cardgame import CardGame
from random import randint


class War(CardGame):

    def __init__(self):
        self.deck = self.create_deck()
        self.deck = self.shuffle_deck(self.deck)

        self.hand1 = []
        self.hand2 = []

        self.dealcards_2players(self.deck, self.hand1, self.hand2)

        self.muck1 = []
        self.muck2 = []
        self.in_play1 = []
        self.in_play2 = []


    def compare_values(self, card1, card2):

        value_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

        figure1, _ = card1.split('.')
        value1 = value_dict[figure1]

        figure2, _ = card2.split('.')
        value2 = value_dict[figure2]

        if value1 > value2:
            return 'player1'
        elif value1 < value2:
            return 'player2'
        elif value1 == value2:
            return 'war'
        else:
            return 'ERROR'


    def war_reveal(self, player, cards_played):
        print(f'{player} has played: ', end=" ")
        for i in range(0, len(cards_played)):
            if i % 2 == 1:
                value, color = cards_played[i].split('.')
                print(f'({value} of {color})', end=" ")
            else:
                value, color = cards_played[i].split('.')
                print(f'{value} of {color}', end=" ")
        print()


    def check_and_play(self, player, hand, muck, in_play, comment=None):
        if hand:
            in_play.insert(0, hand.pop(0))

            if comment:
                    print(comment)

        else:
            if muck:
                hand.extend(self.shuffle_deck(muck))
                muck.clear()
                print(f'{player} has no more cards to play - shuffling his muck.')
                in_play.insert(0, hand.pop(0))

                if comment:
                    print(comment)

            else:
                print(f'{player} has no more cards to play and more more cards in muck.')



    def resolve_round(self, player, muck, in_play1, in_play2):
            muck.extend(in_play1)
            muck.extend(in_play2)
            print(f'{player} wins this round.')
            print()
            
            print('Cards played:')
            self.war_reveal('Player1', in_play1)
            self.war_reveal('Player2', in_play2)

            print(f'Adding cards to {player} muck.')

            in_play1.clear()
            in_play2.clear()


    def round_of_play(self, hand1, muck1, in_play1, hand2, muck2, in_play2):

        self.check_and_play('Player1', hand1, muck1, in_play1)
        self.check_and_play('Player2', hand2, muck2, in_play2)

        value1, figure1 = in_play1[0].split('.')
        value2, figure2 = in_play2[0].split('.')

        print(f'Player1: {value1} of {figure1}')
        print('vs.')
        print(f'Player1: {value2} of {figure2}')
        print()


        result = self.compare_values(in_play1[0], in_play2[0])


        if result == 'player1':
            self.resolve_round('Player1', muck1, in_play1, in_play2)

        elif result == 'player2':
            self.resolve_round('Player2', muck2, in_play1, in_play2)

        elif result == 'war':

            print('WAR!')
            print()

            if not((muck1 or hand1) or (muck2 or hand2)):
                print('There is a war and both players have no cards left to play. Game results in a draw.')
            else:
                self.check_and_play('Player1', hand1, muck1, in_play1, "Player1 places card face-down.")
                self.check_and_play('Player2', hand2, muck2, in_play2, "Player2 places card face-down.")

                print()

                if len(in_play2) == len(in_play2) and (muck1 or hand1) and (muck2 or hand2):
                    self.round_of_play(hand1, muck1, in_play1, hand2, muck2, in_play2)



    def mainloop(self, hand1, muck1, in_play1, hand2, muck2, in_play2):
        
        print('Game begins.')
        no_round = 1
        slicer = '-------'
        print(slicer)
        
        #command = ''

        while((muck1 or hand1) and (muck2 or hand2)): # and command==''
            print(f'Round {no_round} begins.')
            print()
            print('Player1 hand: ', len(hand1))
            print('Player1 muck: ', len(muck1))
            print('Player2 hand: ', len(hand2))
            print('Player2 muck: ', len(muck2))
            print()


            self.round_of_play(hand1, muck1, in_play1, hand2, muck2, in_play2)
            no_round += 1

            print(slicer)

            #command = input('> ')
        print()

        if not(muck1 or hand1) and not(muck2 or hand2):
            print('Such unusual occurence - good job :D')
            print('Everyone loves the chop pot!')
        else:
            if not(muck1 or hand1):
                print('Player1 has no more cards to play and more more cards in muck.')
                print('Player2 wins the game.')
            elif not(muck2 or hand2):
                print('Player2 has no more cards to play and more more cards in muck.')
                print('Player1 wins the game.')

        print()



if __name__ == "__main__":
    game = War()

    game.mainloop(game.hand1, game.muck1, game.in_play1, game.hand2, game.muck2, game.in_play2)
