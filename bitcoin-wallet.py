#!/usr/bin/env python
import sys
import argparse

import balance


"""
For add new mod:
- Create mod file
- Write two functions fill_parser_args(parser: argparse.ArgumentParser), mod_main(args: argparse.Namespace)
- Import it
- Write config in MODS dict
    'mod-name': {
        'description': 'Help message',
        'fill_parser_args': <fill_parser_args(parser)>
        'mod_main': <mod_main(args)>
    },
"""

MODS = {
    'balance': {
        'description': 'Print balance of provided public key (address)',
        'fill_parser_args': balance.fill_parser_args,
        'mod_main': balance.mod_main,
    },
}


def unknown_mod_function(args):
    raise NotImplementedError('Function not set {}'.format(args))


def parse_args():
    """
    For add new mod read head of this file
    """
    parser = argparse.ArgumentParser()
    parser.set_defaults(func=unknown_mod_function)

    mod_parsers = parser.add_subparsers()

    for mod_name, mod in MODS.items():
        mod_parser = mod_parsers.add_parser(mod_name, help=mod['description'])
        mod['fill_parser_args'](mod_parser)
        mod_parser.set_defaults(func=mod['mod_main'])

    return parser.parse_args()


def main():
    args = parse_args()
    return args.func(args)


if __name__ == '__main__':
    sys.exit(main() or 0)

