"""
https://adventofcode.com/2020/day/12
"""


def get_list(file):
    with open(file) as f:
        lines = [(line.rstrip()[0], int(line.rstrip()[1:])) for line in f]
    return lines


def rotate(dir_angle: (str, int), current_dir: str) -> str:
    turn_right = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
    turn_left = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
    dir = dir_angle[0]
    angle = dir_angle[1]
    new_dir = current_dir
    if dir == 'R':
        while angle > 0:
            new_dir = turn_right[new_dir]
            angle -= 90
    else:
        while angle > 0:
            new_dir = turn_left[new_dir]
            angle -= 90
    return new_dir


def rotate2(dir_angle: (str, int), waypoint_position: (int, int)):
    angle = dir_angle[1]
    new_waypoint_position = waypoint_position
    dir1 = 'N' if new_waypoint_position[0] >= 0 else 'S'
    dir2 = 'E' if new_waypoint_position[1] >= 0 else 'W'

    while angle > 0:
        dir1 = rotate(dir_angle, dir1)
        dir2 = rotate(dir_angle, dir2)
        if dir_angle[0] == 'R':
            p1 = 1 if dir1 in ['N', 'S'] else -1
            p2 = 1 if dir2 in ['N', 'S'] else -1
        else:
            p1 = 1 if dir1 in ['E', 'W'] else -1
            p2 = 1 if dir2 in ['E', 'W'] else -1
        new_waypoint_position = new_waypoint_position[1] * p1, new_waypoint_position[0] * p2
        dir1 = 'N' if new_waypoint_position[0] >= 0 else 'S'
        dir2 = 'E' if new_waypoint_position[1] >= 0 else 'W'
        angle -= 90
    return new_waypoint_position


def go_in_direction(direction: (str, int), current_position: (int, int)):
    vertical, horizontal = current_position[0], current_position[1]
    dir = direction[0]
    if dir == 'N':
        vertical += direction[1]
    elif dir == 'S':
        vertical -= direction[1]
    elif dir == 'E':
        horizontal += direction[1]
    elif dir == 'W':
        horizontal -= direction[1]
    return vertical, horizontal


def move_one_step(direction: (str, int), current_direction: str, current_position: (int, int)) -> (str, (int, int)):
    vertical, horizontal = current_position[0], current_position[1]
    new_direction = current_direction
    dir = direction[0]
    if dir in ['N', 'S', 'E', 'W']:
        vertical, horizontal = go_in_direction(direction, current_position)
    elif dir in ['R', 'L']:
        new_direction = rotate((dir, direction[1]), current_direction)
    elif dir == 'F':
        vertical, horizontal = go_in_direction((current_direction, direction[1]), current_position)
    return new_direction, (vertical, horizontal)


def move(steps: [(str, int)], current_direction: str, current_position: (int, int)):
    new_direction, new_position = current_direction, current_position
    for direction in steps:
        new_direction, new_position = move_one_step(direction, new_direction, new_position)
    return new_direction, new_position


def move_forward_to_waypoint(step_value: int, current_position: (int, int), waypoint_position: (int, int)):
    x, y = waypoint_position[0] * step_value, waypoint_position[1] * step_value
    new_position = (current_position[0] + x, current_position[1] + y)
    return new_position


def move2(steps: [(str, int)], current_position: (int, int), waypoint_position: (int, int)):
    new_position = current_position
    new_waypoint_position = waypoint_position
    for direction in steps:
        if direction[0] in ['N', 'S', 'E', 'W']:
            new_waypoint_position = go_in_direction(direction, new_waypoint_position)
        if direction[0] == 'F':
            new_position = move_forward_to_waypoint(direction[1], new_position, new_waypoint_position)
        elif direction[0] in ['R', 'L']:
            new_waypoint_position = rotate2(direction, new_waypoint_position)
    return new_position


def count_manhattan_distance(positions: (int, int)) -> int:
    return abs(positions[0]) + abs(positions[1])


if __name__ == '__main__':
    directions = get_list('input12.txt')
    direction, position = move(directions, 'E', (0, 0))
    manhattan_distance = count_manhattan_distance(position)
    print(manhattan_distance)
    position2 = move2(directions, (0, 0), (1, 10))
    manhattan_distance2 = count_manhattan_distance(position2)
    print(manhattan_distance2)
