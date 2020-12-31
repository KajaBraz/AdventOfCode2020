"""
https://adventofcode.com/2020/day/21
"""
from day4 import get_list
import re
from collections import Counter


def parse_food_list(food: [str]) -> {(str, int): {str}}:
    dishes = {}
    count = 0
    for dish in food:
        ingr_allerg = dish.split('contains')
        ingredients = re.findall(r'\w+', ingr_allerg[0])
        allergens = re.findall(r'\w+', ingr_allerg[1]) + [count]
        dishes[tuple(allergens)] = set(ingredients)
        count += 1
    return dishes


def find_food_with_no_alergens(food: {(str): {str}}) -> [str]:
    alergens = {alergen for multiple_allergens in food.keys() for alergen in multiple_allergens[:-1]}
    ingredients_no_allergens = set().union(*food.values())
    pairs = []
    for alergen in alergens:
        possible_ingr = []
        for k, v in food.items():
            if alergen in k:
                possible_ingr.append(v)
        left = possible_ingr[0]
        for possible in possible_ingr[1:]:
            left = left & possible
        pairs.append((alergen, left))

    found = []
    num_pairs = len(pairs)
    while len(found) < num_pairs:
        for pair in pairs:
            if len(pair[1]) == 1:
                ingredient = pair[1].pop()
                found.append([pair[0], ingredient])
                pairs.remove(pair)
                if ingredient in ingredients_no_allergens:
                    ingredients_no_allergens.remove(ingredient)
                for remaining in pairs:
                    if ingredient in remaining[1]:
                        remaining[1].remove(ingredient)
    count_occurrences = sum(
        [Counter(dish)[ingredient] for dish in food.values() for ingredient in ingredients_no_allergens])
    return found, count_occurrences


def get_ingredients_list_sorted_by_allergen(pairs: [[str]]) -> str:
    sorted_pairs = sorted(pairs)
    return ','.join([pair[1] for pair in sorted_pairs])


if __name__ == '__main__':
    dishes = parse_food_list(get_list('input21.txt'))
    pairs_found, occurrences_ingredients_no_allergens = find_food_with_no_alergens(dishes)  # part 1 solution
    print(occurrences_ingredients_no_allergens)
    ingredients_left = get_ingredients_list_sorted_by_allergen(pairs_found)  # part 2 solution
    print(ingredients_left)
