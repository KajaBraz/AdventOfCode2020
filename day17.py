def get_list(file):
    with open(file) as f:
        lines = [[ch for ch in line.strip()] for line in f]
    return lines


def get_initial_active_coordinates_3D(l: [[str]]) -> {(int)}:
    active = [(x, y, 0) for x in range(len(l)) for y in range(len(l[0])) if l[x][y] == '#']
    return set(active)


def get_initial_active_coordinates_4D(l: [[str]]) -> {(int)}:
    active = [(x, y, 0, 0) for x in range(len(l)) for y in range(len(l[0])) if l[x][y] == '#']
    return set(active)


def get_neighbours_3D(point: ()) -> {(int)}:
    neighbours = set()
    for coor_x in [point[0] - 1, point[0], point[0] + 1]:
        for coor_y in [point[1] - 1, point[1], point[1] + 1]:
            for coor_z in [point[2] - 1, point[2], point[2] + 1]:
                neighbours.add((coor_x, coor_y, coor_z))
    neighbours.remove(point)
    return neighbours


def get_neighbours_4D(point: ()) -> {(int)}:
    neighbours = set()
    for coor_x in [point[0] - 1, point[0], point[0] + 1]:
        for coor_y in [point[1] - 1, point[1], point[1] + 1]:
            for coor_z in [point[2] - 1, point[2], point[2] + 1]:
                for coor_w in [point[3] - 1, point[3], point[3] + 1]:
                    neighbours.add((coor_x, coor_y, coor_z, coor_w))
    neighbours.remove(point)
    return neighbours


def check_grid(initial_grid: [[str]], turns: int, function_neighbours_dimension, function_initial_active):
    active = function_initial_active(initial_grid)
    for turn in range(turns):
        new_active, inactive = set(), set()
        for point in active:
            neighbours = function_neighbours_dimension(point)
            active_neighbours_count = len([True for neighbour in neighbours if neighbour in active])
            if active_neighbours_count in [2, 3]:
                new_active.add(point)
            new_inactive = [neighbour for neighbour in neighbours if neighbour not in active]
            inactive.update(new_inactive)
        for point in inactive:
            neighbours = function_neighbours_dimension(point)
            active_neighbours_count = len([True for neighbour in neighbours if neighbour in active])
            if active_neighbours_count == 3:
                new_active.add(point)
        active = set(new_active)
    return len(active)


if __name__ == '__main__':
    input = get_list('input17.txt')
    print(check_grid(input, 6, get_neighbours_3D,get_initial_active_coordinates_3D))
    print(check_grid(input, 6, get_neighbours_4D,get_initial_active_coordinates_4D))
