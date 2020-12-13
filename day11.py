from day4 import get_list
from collections import Counter


def add_edges(l: [str]):
    with_inner_edges = ['-' + s + '-' for s in l]
    egde = ['-' * len(with_inner_edges[0])]
    with_edges = egde + with_inner_edges + egde
    return with_edges


def is_free(all_seats: [str], seat: (int, int)) -> bool:
    if all_seats[seat[0]][seat[1]] == 'L':
        return True
    return False


def is_occupied(all_seats: [str], seat: (int, int)) -> bool:
    if all_seats[seat[0]][seat[1]] == '#':
        return True
    return False


def free_seats_around(all_seats: [str], adjacent_seats) -> (int, int):
    free_seats = 0
    occupied_seats = 0
    for a in adjacent_seats:
        if is_free(all_seats, a):
            free_seats += 1
        elif is_occupied(all_seats, a):
            occupied_seats += 1
    return free_seats, occupied_seats


def get_closest_occupied(all_seats: [str], seat: (int, int), direction: (int, int)) -> str:
    x, y = seat[0] + direction[0], seat[1] + direction[1]
    while True:
        if 0 < x < len(all_seats) and 0 < y < len(all_seats[0]):
            if all_seats[x][y] == 'L':
                return 'L'
            if all_seats[x][y] == '#':
                return '#'
            x += direction[0]
            y += direction[1]
        else:
            break
    return '.'


def seats_simulation(seats: [str]) -> [str]:
    moved = True
    while moved:
        old_seats = seats[:]
        moved = False
        for row in range(1, len(seats) - 1):
            for column in range(1, len(seats[0]) - 1):
                adjacent_seats = (
                    (row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1), (row + 1, column - 1),
                    (row + 1, column + 1), (row - 1, column - 1), (row - 1, column + 1))
                if is_free(old_seats, (row, column)):
                    if free_seats_around(old_seats, adjacent_seats)[1] == 0:
                        new_s = seats[row][:column] + '#' + seats[row][column + 1:]
                        seats[row] = new_s
                        moved = True
                elif is_occupied(old_seats, (row, column)):
                    if free_seats_around(old_seats, adjacent_seats)[1] >= 4:
                        new_s = seats[row][:column] + 'L' + seats[row][column + 1:]
                        seats[row] = new_s
                        moved = True
    return seats


def seats_simulation2(seats: [str]) -> [str]:
    moved = True
    while moved:
        old_seats = seats[:]
        moved = False
        for row in range(1, len(seats) - 1):
            for column in range(1, len(seats[0]) - 1):
                current_seat = (row, column)
                sides = [
                    get_closest_occupied(old_seats, current_seat, (-1, 0)),
                    get_closest_occupied(old_seats, current_seat, (1, 0)),
                    get_closest_occupied(old_seats, current_seat, (0, -1)),
                    get_closest_occupied(old_seats, current_seat, (0, 1)),
                    get_closest_occupied(old_seats, current_seat, (-1, 1)),
                    get_closest_occupied(old_seats, current_seat, (-1, -1)),
                    get_closest_occupied(old_seats, current_seat, (1, -1)),
                    get_closest_occupied(old_seats, current_seat, (1, 1))
                ]

                if is_free(old_seats, (row, column)):
                    if '#' not in sides:
                        new_s = seats[row][:column] + '#' + seats[row][column + 1:]
                        seats[row] = new_s
                        moved = True
                elif is_occupied(old_seats, (row, column)):
                    occupied = Counter(sides)['#']
                    if occupied >= 5:
                        new_s = seats[row][:column] + 'L' + seats[row][column + 1:]
                        seats[row] = new_s
                        moved = True
    return seats


def count_ch(l: [[str]]) -> int:
    return sum([Counter(row)['#'] for row in l])


if __name__ == '__main__':
    rows = get_list('input11.txt')
    new_rows = add_edges(rows)
    after_simulation = seats_simulation(new_rows)
    print(count_ch(after_simulation))
    after_simulation2 = seats_simulation2(new_rows)
    print(count_ch(after_simulation2))
