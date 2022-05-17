#!/usr/bin/python3

import sys

def capitalCities():
    if len(sys.argv) != 2:
        exit(1)

    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    capital_cities = {v: k for k, v in capital_cities.items()}

    states = {v: k for k, v in states.items()}

    capitalCity = sys.argv[1]

    stateLetters = capital_cities.get(capitalCity)

    if not stateLetters:
        print("Unknown capital city")
        exit()

    state = states.get(stateLetters)
    print(state)


if __name__ == '__main__':
    capitalCities()