"""
https://adventofcode.com/2020/day/15
"""


def initial_turns(nums: [int]) -> {int: [int]}:
    d = {}
    turn = 1
    for num in nums:
        d[num] = [turn]
        turn += 1
    return d


def get_next_num(nums_spoken: {int: [int]}, last_num: int, turn: int) -> ({int: [int]}, int):
    if len(nums_spoken[last_num]) == 1:
        new_num = 0
    else:
        new_num = nums_spoken[last_num][-1] - nums_spoken[last_num][-2]
    if new_num in nums_spoken:
        nums_spoken[new_num].append(turn)
    else:
        nums_spoken[new_num] = [turn]
    return nums_spoken, new_num


def play(initlial_nums: [int], stop_turn) -> int:
    numbers = initial_turns(initlial_nums)
    current_number = initlial_nums[-1]
    for turn in range(len(initlial_nums) + 1, stop_turn + 1):
        numbers, current_number = get_next_num(numbers, current_number, turn)
    return current_number


if __name__ == '__main__':
    input_numbers = [1, 0, 15, 2, 10, 13]
    num_part1 = play(input_numbers, 2020)
    num_part2 = play(input_numbers, 30000000)
    print(num_part1, num_part2)
