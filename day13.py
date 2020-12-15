"""
https://adventofcode.com/2020/day/13
"""
from day4 import get_list
import re


def get_parsed_input(file_name):
    l = get_list(file_name)
    return [int(l[0])] + [[int(n) for n in re.findall(r'\d+', l[1])]]


def get_parsed_input2(file_name):
    l = get_list(file_name)[1].split(',')
    pairs = [(t[0], int(t[1])) for t in enumerate(l) if t[1] != 'x']
    # alternative calculation
    # pairs2 = filter(lambda t: t[1] != 'x', enumerate(l))
    # pairs2 = map(lambda t: (t[0], int(t[1])), pairs2)
    return pairs


def find_your_bus(timestamp: int, bus_timestamps: [int]):
    departures = sorted([((timestamp // bus + 1) * bus, bus) for bus in bus_timestamps])
    to_wait, bus = departures[0][0] - timestamp, departures[0][1]
    return to_wait, bus


def find_earliest_timestamp(buses):
    timestamp = buses[0][1]
    multiplier = timestamp
    for bus in buses[1:]:
        diff = bus[0]
        current_bus = bus[1]
        while (timestamp + diff) % current_bus != 0:
            timestamp += multiplier
        multiplier *= current_bus
    return timestamp


if __name__ == '__main__':
    data = get_parsed_input('input13.txt')
    print(data)
    my_bus = find_your_bus(data[0], data[1])
    print(my_bus[0] * my_bus[1])
    data2 = get_parsed_input2('input13.txt')
    print(data2)
    timestamp = find_earliest_timestamp(data2)
    print(timestamp)
