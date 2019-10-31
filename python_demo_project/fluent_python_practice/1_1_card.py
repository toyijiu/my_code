import collections
from random import choice
Card = collections.namedtuple('Card',['rank','suit'])

#将__len__和__getitem__的具体实现代理给self._card list
class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self,position):
        return self._cards[position]

if __name__ == "__main__":
    deck = FrenchDeck()
    print("the deck size:",len(deck))
    print("the first card:",deck[0])
    print("the last card:",deck[-1])
    print("a random card:",choice(deck))
    print("the first 3 cards:",deck[:3])
    print("all of the A cards:",deck[-1:-5:-1])
    print("all of the cards:")
    for card in deck:
        print(card)
