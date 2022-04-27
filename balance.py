import argparse

import helpers


def fill_parser_args(parser: argparse.ArgumentParser):
    parser.add_argument('-a', '--public-key', type=str, required=True,
        help='Public key (Address) of Bitcoin Wallet')


def mod_main(args: argparse.Namespace):
    print(helpers.get_balance(args.public_key))
    return 0

