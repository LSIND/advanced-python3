#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

class Card:
    '''Represents a playing card'''
    __slots__ = ('suit','rank')
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        '''Returns a string representation'''
        return f'{self.rank} of {self.suit}'

class Deck:
    '''Represents deck of 52 cards.
      cards: list of Card objects.
    '''
    __slots__ = ('__cards',)
    suits = ['spades', 'hearts', 'diamonds', 'clubs']
    ranks = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
    
    def __init__(self):
        self.__cards = []  # private field
        for suit in range(len(self.suits)):
            for rank in range(len(self.ranks)):
                card = Card(self.suits[suit], self.ranks[rank]) # A
                self.__cards.append(card)

    def __str__(self):
        '''Returns a string representation.'''
        res = []
        for card in self.__cards:
            res.append(str(card))
        return '\n'.join(res)

    def shuffle(self):
        '''Shuffle cards in the deck.'''
        random.shuffle(self.__cards)

if __name__ == '__main__':
    print('Sorted deck: ')
    deck = Deck()
    print(deck)
    print('-'*10)
    print('Shuffled deck: ')
    deck.shuffle()
    print(deck)