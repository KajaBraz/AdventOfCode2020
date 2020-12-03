def get_list(file):
    with open(file) as f:
        lines = [line.rstrip() for line in f]
    return lines


def traverse_and_count(step_right: int, step_down: int, list_to_go: [str]) -> int:
    trees = 0
    position_right = step_right
    position_down = step_down
    while position_down < len(list_to_go):
        if position_right >= len(list_to_go[position_down]):
            list_to_go[position_down] *= position_down
        if list_to_go[position_down][position_right] == '#':
            trees += 1
        position_right += step_right
        position_down += step_down
    return trees


if __name__ == '__main__':
    l = get_list('input3.txt')
    encountered_trees = traverse_and_count(3, 1, l)
    print(encountered_trees)
    t1 = traverse_and_count(1, 1, l)
    t2 = traverse_and_count(3, 1, l)
    t3 = traverse_and_count(5, 1, l)
    t4 = traverse_and_count(7, 1, l)
    t5 = traverse_and_count(1, 2, l)
    print(t1, t2, t3, t4, t5)
    print(t1 * t2 * t3 * t4 * t5)
