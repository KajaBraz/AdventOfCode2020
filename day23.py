"""
https://adventofcode.com/2020/day/23
"""


def list_to_dict(numbers: [int]) -> dict:
    current_neighbour_pairs = {num: numbers[ind + 1] for (ind, num) in enumerate(numbers[:-1])}
    current_neighbour_pairs[numbers[-1]] = numbers[0]
    return current_neighbour_pairs


def str_to_list(nums: str) -> [int]:
    return [int(num) for num in nums]


def pick_up(nums: [int]) -> ([int], [int]):
    return [nums[0]] + nums[4:], nums[1:4]


def find_destination(nums: [int]) -> (int, int):
    current = nums[0]
    destination = current - 1
    while destination not in nums[1:]:
        if destination > min(nums[1:]):
            destination -= 1
        else:
            destination = max(nums[1:])
    for ind in range(1, len(nums)):
        if nums[ind] == destination:
            return ind, destination


def find_destination2(picked1, picked2, picked3, current: int, max_val: int) -> int:
    destination = current
    while (destination in [picked1, picked2, picked3, current, 0]):
        destination -= 1
        if destination == 0:
            destination = max_val

    return destination


def insert(picked_up: [int], short_nums: [int], destination_ind: int) -> [int]:
    new_order = [short_nums[ind] for ind in range(1, destination_ind + 1)]
    missing = picked_up + [short_nums[ind] for ind in range(destination_ind + 1, len(short_nums))] + [short_nums[0]]
    new_order.extend(missing)
    return new_order


def play(numbers: [int], rounds: int) -> [int]:
    nums = numbers[:]
    for r in range(rounds):
        temp_nums, picked_up = pick_up(nums)
        destinations_ind, destination = find_destination(temp_nums)
        nums = insert(picked_up, temp_nums, destinations_ind)
    return nums


def play2(numbers: [int], rounds: int) -> [int]:
    nums = list_to_dict(numbers)
    current = numbers[0]
    max_val = max(nums.values())
    for r in range(rounds):
        picked1 = nums[current]
        picked2 = nums[picked1]
        picked3 = nums[picked2]
        destination = find_destination2(picked1, picked2, picked3, current, max_val)
        nums[current] = nums[picked3]
        nums[picked3] = nums[destination]
        nums[destination] = picked1
        current = nums[current]
    r1 = nums[1]
    r2 = nums[r1]
    return r1, r2


if __name__ == '__main__':
    numbers_part1 = str_to_list('538914762')
    numbers_part2 = numbers_part1 + list(range(10, 1000001))
    print(play(numbers_part1, 100))  # part 1 solution
    x1, x2 = play2(numbers_part2, 10000000)
    print(x1 * x2)  # part 2 solution
