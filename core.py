from collections import namedtuple
from random import choice


Deck = namedtuple(
    typename='Deck',
    field_names=['rank', 'suit'],
)


class PlayCard():
    """
    The class abstracts the entity of card decks
    """
    ranks = [str(i) for i in range(2, 11)] + 'J Q K A'.split()
    suits = ['♣️', '♦️', '❤️', '♠️']

    def __init__(self):
        self._cards = [
            Deck(rank, suit)
            for rank in self.ranks
            for suit in self.suits
        ]

    def __getitem__(self, card_index):
        return self._cards[card_index]

    def pick_random_card(self):
        return choice(self._cards)

    def show_random_card(self):
        random_card = self.pick_random_card()
        return f"""
         ___
        |  {random_card.suit}|
        |{random_card.rank
          if random_card.rank == '10'
          else ' ' + random_card.rank} |
        |{random_card.suit}__|
        """

    def __repr__(self):
        return f"{self._cards}"


if __name__ == "__main__":
    my_cards_obj = PlayCard()
    print(my_cards_obj.show_random_card())
