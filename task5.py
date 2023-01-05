# Deck of Cards:
# Создайте класс колоды карт. Внутри колода карт должна использовать другой класс - класс карт. Ваши требования:
# Класс Deck должен иметь метод раздачи для раздачи одной карты из колоды.
# После раздачи карты она удаляется из колоды.
# Должен быть метод «смешивания», который проверяет, что в колоде есть все 52 карты, а затем меняет их случайным образом.
# Класс должен иметь масть (червы, бубны, трефы, пики) и ценность карты (A, 2,3,4,5,6,7,8,9,10, J, Q, K)
# ПРИМЕЧАНИЕ: используйте случайное перемешивание
#
# Copy
# from random import shuffle

import random


class Cards:
    def __init__(self):
        self.card_suit = ('червы', 'бубны', 'трефы', 'пики')
        self.card_values = ('A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K')


class Deck(Cards):
    def __init__(self):
        super().__init__()
        self.deck_cards = []
        for suit in self.card_suit:
            for value in self.card_values:
                self.deck_cards.append(f'{value} {suit}')

    def shuffle(self):
        random.shuffle(self.deck_cards)
        return self.deck_cards

    def deal(self, deal_card):
        if deal_card in self.deck_cards:
            self.deck_cards.remove(deal_card)
        return f'Выдана карта "{deal_card}". Карт в колоде: {len(self.deck_cards)}'


deck = Deck()

print(deck.shuffle())
print(deck.deal('2 пики'))
print()
print(deck.shuffle())
print(deck.deal('K бубны'))
print()
print(deck.shuffle())
print(deck.deal('J трефы'))
print()
print(deck.shuffle())
print(deck.deal('10 червы'))
