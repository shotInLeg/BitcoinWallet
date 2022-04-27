import argparse

import helpers


def fill_parser_args(parser: argparse.ArgumentParser):
    parser.add_argument('-a', '--public-key', type=str, required=True,
        help='Public key (Address) of Bitcoin Wallet')


def mod_main(args: argparse.Namespace):
    wallet_balance = helpers.get_balance(args.public_key)

    print('Bitcoin Wallet: {}'.format(args.public_key))
    print('BTC: {:.8f}'.format(wallet_balance / 100000000))
    print('USD: {}'.format(helpers.convert_to(wallet_balance, 'usd')))
    print('EUR: {}'.format(helpers.convert_to(wallet_balance, 'eur')))
    print('RUB: {}'.format(helpers.convert_to(wallet_balance, 'rub')))

    return 0

