# **************************
# AQUÍ TIENE SU VUELTA (MAX)
# **************************


def run(to_give_back: float, available_currencies: dict) -> dict:
    if to_give_back > 0:
        money_back = {}
        for currency, quantity in sorted(available_currencies.items(), reverse=True):
            quantity_back = 0
            while currency <= to_give_back and quantity > quantity_back:
                to_give_back -= currency
                quantity_back += 1
            money_back[currency] = quantity_back
            if to_give_back <= 0:
                break
        if to_give_back > 0:
            money_back = None
    else:
        money_back = {}

    return money_back


if __name__ == '__main__':
    run(20, {5: 3, 2: 7, 1: 3})
