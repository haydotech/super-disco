from collections import namedtuple
from random import choice

Deck = namedtuple(
    typename='Deck',
    field_names=['rank', 'suit']
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

    def show_card(self, index):
        return f"""
         ___
        |  {self._cards[index].suit}|
        | {self._cards[index].rank} |
        |{self._cards[index].suit}__|
        """

    def show_random_card(self):
        random_card = self.pick_random_card()
        print(random_card)
        # if random_card.rank != '10':
        #     return f"""
        #      ___
        #     |  {random_card.suit}|
        #     | {random_card.rank} |
        #     |{random_card.suit}__|
        #     """
        # else:
        return f"""
         ______
        |     {random_card.suit}|
        |      |
        |  {random_card.rank}   |
        |      |
        |{random_card.suit}_____|
        """

    def __repr__(self):
        return f"{self._cards}"


my_cards_obj = PlayCard()
# print(my_cards_obj.pick_random_card())
# print(my_cards_obj._cards)
# print(my_cards_obj[:3])
# print(my_cards_obj[48:])
# print(len(my_cards_obj._cards))
print(my_cards_obj.show_random_card())
