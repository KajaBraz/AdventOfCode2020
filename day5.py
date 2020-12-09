"""
https://adventofcode.com/2020/day/5
"""
from day4 import get_list


def decipher_row_num(s: str, n_rows: int, n_char) -> int:
    rows = s[:n_char]
    max_position = n_rows - 1
    min_position = 0
    for r in rows[:-1]:
        if r == 'F':
            max_position = max_position - (max_position - min_position) // 2 - 1
        elif r == 'B':
            min_position = min_position + (max_position - min_position) // 2 + 1
    if rows[-1] == 'F':
        return min_position
    elif rows[-1] == 'B':
        return max_position
    return -1


def decipher_column_num(s: str, n_cl: int, n_char) -> int:
    columns = s[len(s) - n_char:]
    max_position = n_cl - 1
    min_position = 0
    for cl in columns[:-1]:
        if cl == 'R':
            min_position = min_position + (max_position - min_position) // 2 + 1
        elif cl == 'L':
            max_position = max_position - (max_position - min_position) // 2 - 1
    if columns[-1] == 'R':
        return max_position
    elif columns[-1] == 'L':
        return min_position
    return -1


def count_seat_ID(row: int, column: int, multiplier: int):
    return row * multiplier + column


def find_seat(IDs: list) -> int:
    ordered = sorted(IDs)
    for i in range(len(ordered) - 2):
        i1 = ordered[i]
        i2 = ordered[i + 1]
        if i2 - i1 == 2:
            return (i2 + i1) // 2
    return -1


if __name__ == '__main__':
    boarding_passes = get_list('input5.txt')
    print(boarding_passes)
    IDs = []
    for bp in boarding_passes:
        row = decipher_row_num(bp, 128, 7)
        column = decipher_column_num(bp, 8, 3)
        IDs.append(count_seat_ID(row, column, 8))
    print(IDs)
    print(max(IDs))
    my_seat = find_seat(IDs)
    print(my_seat)
