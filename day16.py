"""
https://adventofcode.com/2020/day/16
"""
from day4 import get_list
import re
import itertools


def parse_ticket_data(file) -> ({str: [range]}, [[int]]):
    all_data = get_list(file)
    ticket_fields_lines = range(20)
    my_ticket_line = (21)
    nearby_tickets_lines = (24, 264)
    ticket_fields = {}

    for ticket_field in ticket_fields_lines:
        field = re.search(r'[\w\s]+', all_data[ticket_field]).group()
        ranges = [int(n) for n in re.findall(r'\d+', all_data[ticket_field])]
        ranges = [range(ranges[i], ranges[i + 1] + 1) for i in range(len(ranges)) if i % 2 == 0]
        ticket_fields[field] = ranges

    nearby_tickets = [[int(n) for n in re.findall(r'\d+', nearby_ticket)] for nearby_ticket in
                      all_data[nearby_tickets_lines[0] - 1:nearby_tickets_lines[1]]]
    my_ticket = [int(n) for n in re.findall(r'\d+', all_data[my_ticket_line])]
    return ticket_fields, nearby_tickets, my_ticket


def find_invalid(ticket_nums: [[int]], tickets_data: {str: [range]}) -> [(int, int)]:
    ranges = [list(r) for i in tickets_data.values() for r in i]
    ranges = set(itertools.chain(*ranges))
    invalid = [(num, ticket_ind) for ticket_ind in range(len(ticket_nums)) for num in ticket_nums[ticket_ind] if
               num not in ranges]
    return invalid


def get_invalid_sum(invalid_nums: [(int, int)]) -> int:
    invalid = [pair[0] for pair in invalid_nums]
    return sum(invalid)


def get_invalid_indexes(invalid_nums: [(int, int)]) -> [int]:
    return [pair[1] for pair in invalid_nums]


def remove_invalid_tickets(all_tickets: [[int]], invalid_indexes: [int]) -> [[int]]:
    return [all_tickets[ind] for ind in range(len(all_tickets)) if ind not in invalid_indexes]


def find_order(tickets_dict: {str: [range]}, all_tickets: [[int]]):
    field_ind = {}
    fields_order = []
    for field, ranges in tickets_dict.items():
        field_ind[field] = []
        rs = [list(r) for r in ranges]
        possible_nums = set(itertools.chain(*rs))
        for column in range(len(all_tickets[0])):
            correct_values = True
            for row in all_tickets:
                if row[column] not in possible_nums:
                    correct_values = False
            if correct_values:
                field_ind[field].append(column)

    while len(fields_order) < len(field_ind.keys()):
        for field, places in field_ind.items():
            if len(places) == 1:
                val = places[0]
                fields_order.append((field, val))
                for values in field_ind.values():
                    if val in values:
                        values.remove(val)
    return fields_order


def multiply_departure_fields(order: [(str, int)], my_ticket: [int]) -> int:
    res = 1
    for pair in order:
        if re.match(r'departure', pair[0]):
            res *= my_ticket[pair[1]]
    return res


if __name__ == '__main__':
    tickets_fields, nearby_tickets, my_ticket = parse_ticket_data('input16.txt')
    invalid_nums_sum = get_invalid_sum(find_invalid(nearby_tickets, tickets_fields))
    print(invalid_nums_sum)  # part 1 result
    inv = get_invalid_indexes(find_invalid(nearby_tickets, tickets_fields))
    valid = remove_invalid_tickets(nearby_tickets, inv)
    order = find_order(tickets_fields, valid)
    departures_nums_multiplied = multiply_departure_fields(order, my_ticket)
    print(departures_nums_multiplied)  # part 2 result
