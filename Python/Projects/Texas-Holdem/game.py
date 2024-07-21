from cards import *
from roles import *

def get_winner(
    players: list[Player],
    common_cards: list[Card],
    private_cards: list[list[Card]],
    ) -> tuple[Player | None, Hand]:
    dealer = Dealer(players)
    dealer.unveil_common_cards(common_cards)
    dealer.give_private_cards(private_cards)
    return dealer.find_winner()
