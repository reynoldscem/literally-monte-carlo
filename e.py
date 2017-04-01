from itertools import product
import random
import numpy as np

class Deck:
    def __init__(self):
        suits = (
            'Hearts', 'Diamonds',
            'Spades', 'Clubs'
        )
        values = tuple(
            map(str, np.arange(2, 10))
        ) + ('Jack', 'Queen', 'King', 'Ace')
        self.cards = product(
            suits, values
        )

    def shuffle(self):
        temp = list(self.cards)
        random.shuffle(temp)
        self.cards = tuple(temp)

    def pop(self):
        if len(self.cards) <= 1:
            self.cards = ()
        else:
            self.cards = self.cards[1:]

    def first(self):
        return self.cards[0]

    def has_cards(self):
        return len(self.cards) > 0


def trial():
    deck1, deck2 = Deck(), Deck()
    deck1.shuffle(), deck2.shuffle()
    while deck1.has_cards() and deck2.has_cards():
        val1, val2 = deck1.first(), deck2.first()
        deck1.pop(), deck2.pop()
        if val1 == val2:
            return True
    return False


def main():
    matches = 0
    num_trials = 10000

    for i in range(num_trials):
        if trial():
            matches += 1

    print(1 / ((num_trials - matches) / num_trials))


if __name__ == '__main__':
    main()
