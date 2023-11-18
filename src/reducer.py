#!/usr/bin/env python

from itertools import groupby
from operator import itemgetter
import sys


def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator)


def pretty_table(headers, rows):
    # Find the maximum width of each column
    col_widths = [max(len(str(value)) for value in column)
                  for column in zip(*rows, headers)]

    # Print the header row
    header_row = " | ".join(str(title).ljust(
        col_widths[i]) for i, title in enumerate(headers))
    print(header_row)
    print("-" * len(header_row))  # Print a separator

    # Print the data rows
    for row in rows:
        print(" | ".join(str(value).ljust(
            col_widths[i]) for i, value in enumerate(row)))


def main(separator='\t'):
    airline_delays = {}
    airline_names = {}
    data = read_mapper_output(sys.stdin, separator=separator)
    for airline, group in groupby(data, itemgetter(0)):
        try:
            delays = 0
            flights = 0
            for key, data_type, value in group:
                if data_type == 'A':
                    airline_names[key] = value
                    continue
                delays += int(value)
                flights += 1

            avg_delay = delays/flights
            airline_delays[airline] = avg_delay
        except ValueError:
            pass

    top_airlines = sorted(airline_delays.items(),
                          key=lambda x: x[1], reverse=True)[:5]

    headers = ["Airline Code", "Airline Name", "Average Delay"]
    rows = [(airline, airline_names[airline], total_delay)
            for airline, total_delay in top_airlines]

    print("Top 5 airline departure delays:")
    pretty_table(headers, rows)


if __name__ == "__main__":
    main()
