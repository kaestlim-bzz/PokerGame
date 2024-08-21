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



class Player:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.cards = []

    def place_bet(self, betrag):
        if betrag > self.balance:
           print(f'Nicht genug geld nur {self.balance}')
        self.balance -= betrag
        return betrag

    def get_win(self, betrag):
        self.balance += betrag

    def show_balance(self):
        print(f"{self.name}'s aktueller Kontostand: ${self.balance}")

    def add_cards(self, cards):
        self.cards.extend(cards)



class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player("Spieler", 1000)
        self.dealer = Player("Dealer", 1000)
        self.pot = 0

    def bet_round(self):
        bet  = int(input('wie viel möchtest du setzten?'))
        player_bet = self.player.place_bet(bet)
        if player_bet:
            self.pot += player_bet
            print(f'es liegt jetzt {self.pot} im pot')

    def play_game(self):
        self.player.add_cards(self.deck.select_two_player_cards())
        self.dealer.add_cards(self.deck.select_two_dealers_cards())
        self.bet_round()
        if input("Möchtest du weitermachen? (y/n): ").lower() == 'y':
            self.deck.three_flop_cards()
            self.bet_round()
        if input("Möchtest du weitermachen? (y/n): ").lower() == 'y':
            self.deck.one_turn_card()
            self.bet_round()
        if input("Möchtest du weitermachen? (y/n): ").lower() == 'y':
            self.deck.one_river_card()
            self.bet_round()
        self.determine_winner()

    def determine_winner(self):
        print(f"{self.player.name} gewinnt den Pot von ${self.pot}!")
        self.player.get_win(self.pot)
        self.pot = 0
        self.player.show_balance()


game = Game()
game.play_game()

