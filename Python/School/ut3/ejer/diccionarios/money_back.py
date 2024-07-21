# ********************
# AQUÍ TIENE SU VUELTA
# ********************


def run(to_give_back: float, available_currencies: list) -> dict:
    money_back = {}

    if to_give_back:
        sorted_available_currencies = sorted(available_currencies, reverse=True)

        for currency in sorted_available_currencies:
            money_quantity = 0
            while to_give_back >= currency:
                to_give_back -= currency
                money_quantity += 1
            money_back[currency] = money_quantity
            if to_give_back <= 0:
                break

        if to_give_back:
            money_back = None

    return money_back


if __name__ == '__main__':
    run(20, [5, 2, 1])
