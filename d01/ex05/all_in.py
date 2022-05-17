#!/usr/bin/env python3
# -*-coding:utf-8 -*

import sys

def find_val_by_key(cle, dic):
    for key, value in dic.items():
        if cle.lower() == key.lower():
            return value
    return None

def find_key_by_val(val, dic):
    for key, value in dic.items():
        if value.lower() == val.lower():
            return key
    return None

def getCc(state, stLetters, capital_cities):
    capital = find_val_by_key(stLetters, capital_cities)

    print(capital, "is the capital of", state)

def getSt(capital, ccLetters, states):
    state = find_key_by_val(ccLetters, states)

    print(capital, "is the capital of", state)

def arrParser(arr, st, cc):
    for item in arr:
        item = item.strip()

        if len(item) > 0:
            stLetters = find_val_by_key(item, st)
            ccLetters = find_key_by_val(item, cc)

            if not stLetters and not ccLetters:
                print(item, "is neither a capital city nor a state")

            if stLetters:
                state = find_key_by_val(stLetters, st)
                getCc(state, stLetters, cc)
            elif ccLetters:
                capital = find_val_by_key(ccLetters, cc)
                getSt(capital, ccLetters, st)

def allIn():
    if len(sys.argv) != 2:
        exit()

    states = {
            "Oregon"    : "OR",
            "Alabama"   : "AL",
            "New Jersey": "NJ",
            "Colorado"  : "CO"
            }

    capital_cities = {
            "OR": "Salem",
            "AL": "Montgomery",
            "NJ": "Trenton",
            "CO": "Denver"
            }

    arr = sys.argv[1].split(",")

    arrParser(arr, states, capital_cities)

if __name__ == '__main__':
    allIn()