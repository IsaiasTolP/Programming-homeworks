from __future__ import annotations
from helpers import *

class Card:
    RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
    SUITS = ('❤', '◆', '♣', '♠')

    def __init__(self, value: str) -> None:
        self.value = value
        self.rank = value[:-1]
        self.suit = value[-1]

    def __gt__(self: Card, other: Card) -> bool:
        return Card.RANKS.index(self.rank) > Card.RANKS.index(other.rank)

class Deck:
    def __init__(self) -> None:
        self.cards = [f'{rank}{suit}' for suit in Card.SUITS for rank in Card.RANKS]
        shuffle(self.cards)

class Hand:
    HAND_LENGTH = 5
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8

    def __init__(self, cards: list[Card]) -> None:
        self.cards = sorted(cards)
        self.hand_ranks = tuple(card.rank for card in self)
        self.hand_suits = tuple(card.suit for card in self)
        self.cat = self.get_cat()

    def is_straight_flush(self) -> bool:
        if len(set(self.hand_suits)) == 1:
            cmp_start = Card.RANKS.index(self[0].rank)
            return self.hand_ranks == Card.RANKS[cmp_start : cmp_start + Hand.HAND_LENGTH]
        return False

    def is_four_of_a_kind(self) -> bool:
        for rank in self.hand_ranks:
            if self.hand_ranks.count(rank) >= 4:
                self.cat_rank = rank
                return True
        return False

    def is_full_house(self) -> bool:
        unique_ranks = set(self.hand_ranks)
        if len(unique_ranks) == 2:
            self.cat_rank = []
            for rank in unique_ranks:
                if self.hand_ranks.count(rank) == 3:
                    self.cat_rank.insert(0, rank)
                else:
                    self.cat_rank.append(rank)
            self.cat_rank = tuple(self.cat_rank)
            return True
        return False

    def is_flush(self) -> bool:
        return len(set(self.hand_suits)) == 1

    def is_straight(self) -> bool:
        cmp_start = Card.RANKS.index(self[0].rank)
        return self.hand_ranks == Card.RANKS[cmp_start : cmp_start + Hand.HAND_LENGTH]

    def is_three_of_a_kind(self) -> bool:
        for rank in self.hand_ranks:
            if self.hand_ranks.count(rank) == 3:
                self.cat_rank = rank
                return True
        return False

    def is_two_pair(self) -> bool:
        pairs = 0
        ranks_idxs = []
        for rank in set(self.hand_ranks):
            if self.hand_ranks.count(rank) == 2:
                pairs += 1
                ranks_idxs.append(Card.RANKS.index(rank))
                if pairs == 2:
                    ranks_idxs = sorted(ranks_idxs, reverse=True)
                    self.cat_rank = tuple(Card.RANKS[i] for i in ranks_idxs)
                    return True
        return False

    def is_one_pair(self) -> bool:
        for rank in self.hand_ranks:
            if self.hand_ranks.count(rank) == 2:
                self.cat_rank = rank
                return True
        return False

    def get_cat(self) -> int:
        if self.is_straight_flush():
            cat = Hand.STRAIGHT_FLUSH
            self.cat_rank = self[-1].rank
        elif self.is_four_of_a_kind():
            cat = Hand.FOUR_OF_A_KIND
        elif self.is_full_house():
            cat = Hand.FULL_HOUSE
        elif self.is_flush():
            cat = Hand.FLUSH
            self.cat_rank = self[-1].rank
        elif self.is_straight():
            cat = Hand.STRAIGHT
            self.cat_rank = self[-1].rank
        elif self.is_three_of_a_kind():
            cat = Hand.THREE_OF_A_KIND
        elif self.is_two_pair():
            cat = Hand.TWO_PAIR
        elif self.is_one_pair():
            cat = Hand.ONE_PAIR
        else:
            cat = Hand.HIGH_CARD
            self.cat_rank = self[-1].rank
        return cat

    def __contains__(self: Hand, card: Card) -> bool:
        return card.value in tuple(card.value for card in self)
    
    def __gt__(self: Hand, other: Hand) -> bool | None:
        if self.cat == other.cat:
            if self.cat_rank == other.cat_rank:
                for card1, card2 in zip(self[::-1], other[::-1]):
                    if card1 > card2:
                        return True
                    elif card1.rank == card2.rank:
                        continue
                    else:
                        return False
            if isinstance(self.cat_rank, tuple):
                hand1_cat_ranks, hand2_cat_ranks = tuple(Card.RANKS.index(rank) for rank in self.cat_rank), tuple(Card.RANKS.index(rank) for rank in other.cat_rank)
                if self.cat == Hand.FULL_HOUSE:
                    return hand1_cat_ranks[0] * 3 + hand1_cat_ranks[1] * 2 > hand2_cat_ranks[0] * 3 + hand2_cat_ranks[1] * 2
                else:
                    return hand1_cat_ranks[0] * 2 + hand1_cat_ranks[1] * 2 > hand2_cat_ranks[0] * 2 + hand2_cat_ranks[1] * 2
            else:
                return Card.RANKS.index(self.cat_rank) > Card.RANKS.index(other.cat_rank)
        return self.cat > other.cat
    
    def __getitem__(self, index: int):
        return self.cards[index]
    
    def __iter__(self):
        return HandIterator(self)


class HandIterator:
    def __init__(self, hand: Hand) -> None:
        self.hand = hand
        self.pointer = 0
    
    def __next__(self):
        if self.pointer >= len(self.hand.cards):
            raise StopIteration
        else:
            item = self.hand[self.pointer]
            self.pointer += 1
            return item
