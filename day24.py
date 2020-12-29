from day4 import get_list


def get_coordinates(directions_to_go: str) -> (int, int):
    directions = {'e': (0, 1), 'se': (-1, .5), 'sw': (-1, -.5), 'w': (0, -1), 'nw': (1, -.5), 'ne': (1, .5)}
    position = [0, 0]
    current = 0
    while current < len(directions_to_go):
        direction = directions_to_go[current]
        if direction not in directions:
            direction = directions_to_go[current:current + 2]
            current += 1
        position[0] += directions[direction][0]
        position[1] += directions[direction][1]
        current += 1
    return tuple(position)


def black_tiles(directions_list: [str]) -> set:
    black_tiles = set()
    coordinates = list(map(get_coordinates, directions_list))
    for tile_position in coordinates:
        if tile_position not in black_tiles:
            black_tiles.add(tile_position)
        else:
            black_tiles.remove(tile_position)
    return black_tiles


def get_neighbours(tile: (int, int)) -> {(int, int)}:
    directions = {'e': (0, 1), 'se': (-1, .5), 'sw': (-1, -.5), 'w': (0, -1), 'nw': (1, -.5), 'ne': (1, .5)}
    neighbours = []
    for direction in directions:
        neighbours.append((tile[0] + directions[direction][0], tile[1] + directions[direction][1]))
    return set(neighbours)


def apply_rules(current_black_tiles: set, steps: int) -> int:
    new_white, new_black = set(), set()
    black_tiles = current_black_tiles.copy()
    white_tiles = set()
    for step in range(steps):
        for black_tile in black_tiles:
            all_neighbours = get_neighbours(black_tile)
            black_neighbours = all_neighbours & black_tiles
            white_neighbours = all_neighbours - black_tiles
            white_tiles.update(white_neighbours)
            if 0 < len(black_neighbours) <= 2:
                new_black.add(black_tile)
        for white_tile in white_tiles:
            all_neighbours = get_neighbours(white_tile)
            black_neighbours = all_neighbours & black_tiles
            if len(black_neighbours) == 2:
                new_black.add(white_tile)
        black_tiles = new_black.copy()
        white_tiles.clear()
        new_black.clear()
    return len(black_tiles)


if __name__ == '__main__':
    directions = get_list('input24.txt')
    black_tiles = black_tiles(directions)
    print(len(black_tiles))  # part 1 solution
    black_num = apply_rules(black_tiles, 100)
    print(black_num)  # part 2 solution
