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

    state = sys.argv[1]

    stateLetters = states.get(state)

    if not stateLetters:
        print("Unknown state")
        exit()

    captialCity = capital_cities.get(stateLetters)
    print(captialCity)


if __name__ == '__main__':
    capitalCities()