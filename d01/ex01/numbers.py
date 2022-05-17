#!/usr/bin/python3

def read_target():
    f = open("numbers.txt", 'r')
    for line in f.readlines():
        print_line(line.strip())
    f.close()


def print_line(line: str):
    nodes = line.split(",")
    for node in nodes:
        print(node)


if __name__ == '__main__':
    read_target()