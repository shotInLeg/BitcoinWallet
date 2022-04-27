from bit.network import NetworkAPI, satoshi_to_currency


def get_balance(public_key, currency='usd'):
    return satoshi_to_currency(NetworkAPI.get_balance(public_key), currency)

