"""
https://adventofcode.com/2020/day/9
"""


def get_numbers_list(file) -> [int]:
    with open(file) as f:
        lines = [int(line.strip()) for line in f]
    return lines


def sum_in_cycle(cycle_range: int, l: [int], num_ind: int) -> bool:
    searched_sum = l[num_ind]
    possibilities = set(l[num_ind - cycle_range:num_ind])
    for p in possibilities:
        if searched_sum - p in possibilities and searched_sum - p != searched_sum:
            return True
    return False


def sum_in_cycle2(cycle_range: int, l: [int], num_ind: int) -> bool:
    searched_sum = l[num_ind]
    possibilities = sorted(l[num_ind - cycle_range:num_ind])
    i, j = 0, len(possibilities) - 1
    for n in possibilities:
        if possibilities[i] + possibilities[j] == searched_sum:
            return True
        elif possibilities[i] + possibilities[j] < searched_sum:
            i += 1
        elif possibilities[i] + possibilities[j] > searched_sum:
            j -= 1
    return False


def get_num_sum_not_in_cycle(cycle_range: int, l: [int]) -> (int, int):
    for n_ind in range(cycle_range, len(nums)):
        if not sum_in_cycle(cycle_range, l, n_ind):
            return n_ind, l[n_ind]
    return -1, -1


def find_contiguous_set(l: [int], target: int) -> [int]:
    nums = [0]
    start_num_ind, nth_num_ind = 0, 1
    while start_num_ind < len(l) - 1:
        for n in l[start_num_ind:]:
            if sum(nums) <= target:
                nums.append(n)
                if sum(nums) == target:
                    return nums
        nums = []
        start_num_ind += 1
    return nums


def get_sum(l: [int]):
    return min(l) + max(l)


if __name__ == '__main__':
    cycle = 25
    nums = get_numbers_list('input9.txt')
    print(nums)
    i, n = get_num_sum_not_in_cycle(cycle, nums)
    print(i, n)
    cs = find_contiguous_set(nums, n)
    print(cs)
    res = get_sum(cs)
    print(res)
