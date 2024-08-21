import random

class Card:
    def __init__(self, rank, suit, ascii_art):
        self.rank = rank
        self.suit = suit
        self.ascii_art = ascii_art


    def show(self):
        print(self.ascii_art)

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    @staticmethod
    def create_deck():
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        cards = []
        for suit in suits:
            for rank in ranks:
                ascii_art = f"┌───────┐\n│ {rank:<2}    │\n│       │\n│   {suit[0]}   │\n│       │\n│    {rank:>2} │\n└───────┘"
                cards.append(Card(rank, suit, ascii_art))
        return cards


class Deck:
    def __init__(self):
        self.cards = Card.create_deck()

    def select_two_player_cards(self):
        random_elements = random.choices(self.cards, k=2)
        print('Your Cards are:')
        for card in random_elements:
            self.cards.remove(card)
            card.show()
        return random_elements

    def select_two_dealers_cards(self):
        random_dealer = random.choices(self.cards, k=2)
        for card in random_dealer:
            self.cards.remove(card)
        return random_dealer

    def three_flop_cards(self):
        random_flop = random.choices(self.cards, k=3)
        print('The Flop is:')
        for card in random_flop:
            self.cards.remove(card)
            card.show()
        return random_flop

    def one_turn_card(self):
        random_turn = random.choices(self.cards, k=1)
        print('The Turn is:')
        for card in random_turn:
            self.cards.remove(card)
            card.show()
        return random_turn

    def one_river_card(self):
        random_river = random.choices(self.cards, k=1)
        print('The River is:')
        for card in random_river:
            self.cards.remove(card)
            card.show()

        return random_river


# Beispiel Nutzung
deck = Deck()
deck.select_two_player_cards()
deck.select_two_dealers_cards()
nextCard = input('Do you want to countine, anwser with y/n:')
if nextCard == 'y':
    deck.three_flop_cards()
    turnCard = input('Do you want to countine, anwser with y/n:')
    if turnCard == 'y':
        deck.one_turn_card()
        riverCard = input('Do you want to countine, anwser with y/n:')
        if riverCard == 'y':
            deck.one_river_card()

