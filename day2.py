from collections import Counter


def get_list(file):
    with open(file) as f:
        lines = [line.rstrip().split(' ') for line in f]
    return lines


def parse_data(l: [str, str, str]) -> [int, int, str, str]:
    occurence_range = l[0].split('-')
    a, b = int(occurence_range[0]), int(occurence_range[1])
    c = l[1][:-1]
    d = l[2]
    return [a, b, c, d]


def check(min_num: int, max_num: int, character: str, password: str) -> bool:
    occ_num = Counter(password)[character]
    if occ_num >= min_num and occ_num <= max_num:
        return True
    return False


def check2(ind1: int, ind2: int, character: str, password: str) -> bool:
    if (password[ind1 - 1] == character) + (password[ind2 - 1] == character) == 1:
        return True
    return False


if __name__ == '__main__':
    passwords = get_list('input2.txt')
    print(passwords)
    passwords_cleared = [parse_data(i) for i in passwords]
    print(passwords_cleared)
    checked = [check(i[0], i[1], i[2], i[3]) for i in passwords_cleared]
    print(checked)
    print(sum(checked))
    checked2 = [check2(i[0], i[1], i[2], i[3]) for i in passwords_cleared]
    print(checked2)
    print(sum(checked2))
