def get_list(file):
    with open(file) as f:
        lines = [int(line.rstrip()) for line in f]
    return lines


def find_pair(num_list: list, nums_sum: int) -> (int, int):
    nums = sorted(num_list)
    i, j = 0, len(nums) - 1
    while True:
        if nums[i] + nums[j] == nums_sum:
            return (nums[i], nums[j])
        elif nums[i] + nums[j] > nums_sum:
            j -= 1
        elif nums[i] + nums[j] < nums_sum:
            i += 1
        else:
            return (-1, -1)


def find_triple(num_list: list, num_sum: int):
    for i in num_list:
        for j in num_list:
            for k in num_list:
                if i != j and i != k:
                    if i + j + k == num_sum:
                        return i, j, k
    return -1, -1, -1


def multiply(nums):
    res = 1
    for n in nums:
        res *= n
    return res


if __name__ == '__main__':
    number_l = get_list('input1.txt')
    p = find_pair(number_l, 2020)
    print(p, sum(p))
    print('pair', multiply(p))
    t = find_triple(number_l, 2020)
    print(t, sum(t))
    print('triple', multiply(t))
