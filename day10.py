"""
https://adventofcode.com/2020/day/10
"""
from day9 import get_numbers_list


def count_diff(l: [int]) -> {}:
    diff = {'1': 0, '2': 0, '3': 0}
    all_nums_ordered = [0] + sorted(l) + [max(l) + 3]
    for i in range(len(all_nums_ordered) - 1):
        current_diff = all_nums_ordered[i + 1] - all_nums_ordered[i]
        if current_diff == 1:
            diff['1'] += 1
        elif current_diff == 2:
            diff['2'] += 1
        elif current_diff == 3:
            diff['3'] += 1
        else:
            return None
    return diff


def count_connections(sorted_l: [int], results) -> int:
    if len(sorted_l) <= 2:
        return 1
    if tuple(sorted_l) in results:
        return results[tuple(sorted_l)]
    if sorted_l[1] - sorted_l[0] in [1, 2] and (sorted_l[2] - sorted_l[0] in [2, 3]):
        r = count_connections(sorted_l[1:], results) + count_connections([sorted_l[0]] + sorted_l[2:], results)
        results[tuple(sorted_l)] = r
        return r
    r = count_connections(sorted_l[1:], results)
    results[tuple(sorted_l)] = r
    return r


# slow version
def count_connections2(sorted_l: [int]) -> int:
    if len(sorted_l) <= 2:
        return 1
    if sorted_l[1] - sorted_l[0] in [1, 2] and (sorted_l[2] - sorted_l[0] in [2, 3]):
        return count_connections2(sorted_l[1:]) + count_connections2([sorted_l[0]] + sorted_l[2:])
    return count_connections2(sorted_l[1:])


def multiply(l: [int]) -> int:
    res = 1
    for i in l:
        res *= i
    return res


if __name__ == '__main__':
    output_joltage_l = get_numbers_list('input10.txt')
    print(output_joltage_l)
    diffs = count_diff(output_joltage_l)
    print(diffs)
    task_1_res = multiply([diffs['1'], diffs['3']])
    print(task_1_res)
    print(count_connections(sorted([0] + output_joltage_l), {}))
