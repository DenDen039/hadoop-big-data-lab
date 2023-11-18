#!/usr/bin/env python
import sys


def read_input(file, separator):
    for line in file:
        yield line.split(',')


def main(separator=','):
    data = read_input(sys.stdin, separator)
    for words in data:
        if words[0] == 'YEAR' or words[0] == 'IATA_CODE':
            continue

        if len(words) == 2:
            print(f"{words[0]}\tA\t{words[1]}")
            continue

        airline = words[4]
        delay = words[11]

        if delay:
            print(f"{airline}\tF\t{delay}")


if __name__ == "__main__":
    main()
