from bit.network import NetworkAPI, satoshi_to_currency


def get_balance(public_key):
    return NetworkAPI.get_balance(public_key)


def convert_to(balance, currency='usd'):
    return satoshi_to_currency(balance, currency)

