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
        result = ''

        figure1, _ = card1.split('.')
        value1 = value_dict[figure1]

        figure2, _ = card2.split('.')
        value2 = value_dict[figure2]

        if value1 > value2:
            result = 'player1'
        elif value1 < value2:
            result = 'player2'
        elif value1 == value2:
            result = 'war'
        else:
            result = 'ERROR'
        
        return result


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


    def round_of_play(self, hand1, muck1, in_play1, hand2, muck2, in_play2):

        if hand1:
            in_play1.insert(0, hand1.pop(0))
        else:
            if muck1:
                hand1.extend(self.shuffle_deck(muck1))
                muck1.clear()
                print('Player1 has no more cards to play - shuffling his muck.')

                in_play1.insert(0, hand1.pop(0))
            else:
                print('Player1 has no more cards to play and more more cards in muck.')
                print('Player2 wins the game.')
        
        if hand2:
            in_play2.insert(0, hand2.pop(0))
        else:
            if muck2:
                hand2.extend(self.shuffle_deck(muck2))
                muck2.clear()
                print('Player2 has no more cards to play - shuffling his muck.')

                in_play2.insert(0, hand2.pop(0))
            else:
                print('Player2 has no more cards to play and more more cards in muck.')
                print('Player1 wins the game.')


        value1, figure1 = in_play1[0].split('.')
        value2, figure2 = in_play2[0].split('.')
        print(f'Player1: {value1} of {figure1}')
        print('vs.')
        print(f'Player1: {value2} of {figure2}')
        print()

        result = self.compare_values(in_play1[0], in_play2[0])

        if result == 'player1':
            muck1.extend(in_play1)
            muck1.extend(in_play2)
            print('Player1 wins this round.')
            print()
            
            print('Cards played:')
            self.war_reveal('Player1', in_play1)
            self.war_reveal('Player2', in_play2)

            print('Adding cards to Player1 muck.')

            in_play1.clear()
            in_play2.clear()

        elif result == 'player2':
            muck2.extend(in_play1)
            muck2.extend(in_play2)
            print('Player2 wins this round.')
            print()
            
            print('Cards played:')
            self.war_reveal('Player1', in_play1)
            self.war_reveal('Player2', in_play2)
            

            print('Adding cards to Player2 muck.')

            in_play1.clear()
            in_play2.clear()

        elif result == 'war':

            print('WAR!')
            print()

            if not((hand1 or muck1) or (hand2 or muck2)):
                print('There is a war and both players have no cards left to play. Game results in a draw.')
            else:
                if hand1:
                    in_play1.insert(0, hand1.pop(0))
                    print('Player1 places card face-down.')
                else:
                    if muck1:
                        hand1.extend(self.shuffle_deck(muck1))
                        muck1.clear()
                        print('Player1 has no more cards to play - shuffling his muck.')

                        in_play1.insert(0, hand1.pop(0))
                        print('Player1 places card face-down.')
                    else:
                        print('Player1 has no more cards to play and more more cards in muck and there is a war.')
                        print('Player2 wins the game.')
                
                if hand2:
                    in_play2.insert(0, hand2.pop(0))
                    print('Player2 places card face-down.')
                else:
                    if muck2:
                        hand2.extend(self.shuffle_deck(muck2))
                        muck2.clear()
                        print('Player2 has no more cards to play - shuffling his muck.')

                        in_play2.insert(0, hand2.pop(0))
                        print('Player2 places card face-down.')
                    else:
                        print('#Player2 has no more cards to play and more more cards in muck and there is a war.')
                        print('Player1 wins the game.')

                print()
                self.round_of_play(hand1, muck1, in_play1, hand2, muck2, in_play2)


    def mainloop(self, hand1, muck1, in_play1, hand2, muck2, in_play2):
        
        print('Game begins.')
        no_round = 1
        slicer = '-------'
        print(slicer)
        
        command = ''

        while((hand1 or muck1) and (hand2 or muck2) and command==''):
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

        if not(hand1 or muck1) and not(hand2 or muck2):
            print('Such unusual occurence - good job :D')
            print('Everyone loves the chop pot!')
        else:
            if not(hand1 or muck1):
                print('Player1 has no more cards to play and more more cards in muck.')
                print('Player2 wins the game.')
            elif not(hand2 or muck2):
                print('Player2 has no more cards to play and more more cards in muck.')
                print('Player1 wins the game.')


        print()



if __name__ == "__main__":
    game = War()

    #returny i kody zwycięstw do zrobienia
    # bo teraz jest most of time ok, ale może się zdarzyć syf
    # wojna na ostatniej karcie

    game.mainloop(game.hand1, game.muck1, game.in_play1, game.hand2, game.muck2, game.in_play2)
