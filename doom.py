#!/usr/bin/env python3

import argparse
import random
from datetime import datetime


def train():
    print("=== Training Mode ===")
    year = random.randint(1900, 2100)
    month = random.randint(1, 12)
    day = random.randint(1, 28)

    print(f"Date: {month}/{day}/{year}")
    answer = input("Weekday? > ")

    actual = datetime(year, month, day).strftime("%A")

    if answer.strip().lower() == actual.lower():
        print("✓ Correct")
    else:
        print(f"✗ Incorrect")
        print(f"Answer: {actual}")


def speed():
    print("=== Speed Mode ===")
    print("You have 10 dates. Time yourself.")
    print("(Implementation coming soon)")


def anchors():
    print("=== Doomsday Anchor Dates ===")
    print("""
Common Doomsday Dates

4/4
6/6
8/8
10/10
12/12

5/9
9/5

7/11
11/7

March 14
January 3 (normal years)
January 4 (leap years)
February 28 (normal years)
February 29 (leap years)
""")


def stats():
    print("=== Statistics ===")
    print("Games Played : 0")
    print("Accuracy     : 0%")
    print("Best Streak  : 0")
    print("Average Time : N/A")


def main():
    parser = argparse.ArgumentParser(
        prog="doom",
        description="Train the Doomsday Algorithm."
    )

    subparsers = parser.add_subparsers(
        dest="command",
        help="Available commands"
    )

    subparsers.add_parser(
        "train",
        help="Practice random dates"
    )

    subparsers.add_parser(
        "speed",
        help="Timed challenge mode"
    )

    subparsers.add_parser(
        "anchors",
        help="View doomsday anchor dates"
    )

    subparsers.add_parser(
        "stats",
        help="View training statistics"
    )

    args = parser.parse_args()

    if args.command == "train":
        train()
    elif args.command == "speed":
        speed()
    elif args.command == "anchors":
        anchors()
    elif args.command == "stats":
        stats()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()