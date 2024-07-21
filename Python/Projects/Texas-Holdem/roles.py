from __future__ import annotations
from cards import *
from helpers import combinations

class Player:
    def __init__(self, name: str) -> None:
        self.name = name

    def receive_private_cards(self, cards: list[Card]):
        self.private_cards = cards

    def find_combinations(self):
        all_cards = self.private_cards + Dealer.COMMON_CARDS
        return combinations(all_cards, n=5)
    
    def find_higher_hand(self) -> Hand:
        combinations = (self.find_combinations())
        all_hands = (Hand(hand) for hand in combinations)
        return max(all_hands)
    
    def __str__(self) -> str:
        return self.name

class Dealer:
    def __init__(self, players: list[Player]) -> None:
        self.players = players

    def give_private_cards(self, cards: list[list[Card]]):
        for i, player in enumerate(self.players):
            player.receive_private_cards(cards=cards[i])

    @classmethod
    def unveil_common_cards(cls, cards: list[Card]):
        cls.COMMON_CARDS = cards

    def find_winner(self) -> tuple[Player | None, Hand]:
        hand1, hand2 = self[0].find_higher_hand(), self[1].find_higher_hand()
        if hand1 > hand2:
            return self[0], hand1 
        elif hand2 > hand1:
            return self[1], hand2
        else:
            return None, hand1

    def __getitem__(self, index: int) -> Player:
        return self.players[index]
