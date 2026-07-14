from backlog import core

import random
import argparse


def main():
    parser = argparse.ArgumentParser(
        prog="backlog", 
        description="A commmand line tool to manage your backlog of games",
        )
    subparsers = parser.add_subparsers(
        dest="command", 
        required= True,
        )

    # ADD  
    add_parser = subparsers.add_parser(
        "add", 
        help="Add a game to your backlog"),
    add_parser.add_argument(
        "titles", 
        nargs="+", 
        help="Title(s) of the game(s) to add",
        )
    add_parser.add_argument(
        "--platform", 
        help="Platform of the game(s) to add: PC, PS5, Xbox, Switch",
        )
    #add_parser.add_argument("--tag", action="append", dest="tags", default=[])

    # LIST 
    list_parser = subparsers.add_parser(
        "list", 
        help="List all games in your backlog",
        )

    # ROLL
    roll_parser = subparsers.add_parser(
        "roll", 
        help="Roll for a random game",
        )

    args = parser.parse_args()
    if args.command == "add":
        core.add_games(args.titles, args.platform)
    elif args.command == "list":
        core.list_games()
    elif args.command == "roll":
        core.roll_game()

if __name__ == "__main__":
    main()