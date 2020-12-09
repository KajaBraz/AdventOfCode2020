"""
https://adventofcode.com/2020/day/7
"""
import re
from day4 import get_list


def get_dict(l: [str]) -> {}:
    bags = {}
    for s in l:
        bags_colours = s.split('bags contain')
        k = bags_colours[0].strip()
        values = re.findall(r'(\d+)([\s\w]*)', bags_colours[1])
        values = [(int(n), re.sub(r'bags?', '', c).strip()) for n, c in values]
        bags[k] = values
    return bags


def dict_only_colours(d: dict) -> dict:
    only_colours = {}
    for k, v in d.items():
        only_colours[k] = [colour for num, colour in v]
    return only_colours


def flatten(nested_list):
    if len(nested_list) == 0:
        return []
    if isinstance(nested_list[0], list):
        return flatten(nested_list[0]) + flatten(nested_list[1:])
    return nested_list[:1] + flatten(nested_list[1:])


def find_outer(colour: str, bags: dict):
    return [[outer_colour] + find_outer(outer_colour, bags) for outer_colour, inner_colours in bags.items() if
            colour in inner_colours]


def count_inner(colour: str, bags: {str: [(int, str)]}) -> [int]:
    if len(bags[colour]) == 0: return 0
    return sum([c[0] + c[0] * count_inner(c[1], bags) for c in bags[colour]])


if __name__ == '__main__':
    l = get_list('input7.txt')
    print(l)
    bags_dict = get_dict(l)
    print(bags_dict)
    bags_colours = dict_only_colours(bags_dict)
    print(bags_colours)
    check_colour = find_outer('shiny gold', bags_colours)
    fl = flatten(check_colour)
    outer_colours = set(fl)
    print(outer_colours)
    print(len(outer_colours))
    inner_count = count_inner('shiny gold', bags_dict)
    print(inner_count)
