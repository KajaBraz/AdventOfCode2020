import re
import functools
from pprint import pprint


def parse_tiles(file) -> ([int], [int]):
    data = open(file, 'r').read()
    numbers = [int(id) for id in re.findall(r'\d+', data)]
    tiles = re.findall(r'[.#]+', data)
    grouped = []
    for n in range(len(numbers)):
        n_rows = 0
        rows = []
        while n_rows < 10:
            rows.append(tiles[n * 10 + n_rows])
            n_rows += 1
        grouped.append(rows)
    return numbers, grouped


def get_edges(tile: [str]) -> []:
    edges = [tile[0], tile[-1]]
    right, left = '', ''
    for i in (tile):
        left += i[0]
        right += i[-1]
    edges.extend([left, right])
    return edges  # edges positions: up, down, left, right


def join_tiles(tiles: [[str]], ids_list:[int]):
    all_edges = [get_edges(tile) for tile in tiles]
    joined_pairs = set()
    for e1 in range(len(all_edges)):
        for e2 in range(len(all_edges)):
            if e1 != e2:
                for edge1 in all_edges[e1]:
                    for edge2 in all_edges[e2]:
                        if edge1 == edge2 or edge1 == edge2[::-1]:
                            p1 = (ids_list[e1], edge1, all_edges[e1].index(edge1)) if e1 < e2 else (ids_list[e2], edge2, all_edges[e2].index(edge2))  # first tuple item: tile index, second tuple item: edge, third tuple item: edge position
                            p2 = (ids_list[e2], edge2, all_edges[e2].index(edge2)) if e1 < e2 else (ids_list[e1], edge1, all_edges[e1].index(edge1))
                            joined_pairs.add((p1, p2))
    return joined_pairs


def get_corners_ids(paired_edges: [{((int, str))}]) -> [int]:
    occurrences = {}
    corners = []
    for pair in paired_edges:
        if pair[0][0] in occurrences:
            occurrences[pair[0][0]] += 1
        else:
            occurrences[pair[0][0]] = 1
        if pair[1][0] in occurrences:
            occurrences[pair[1][0]] += 1
        else:
            occurrences[pair[1][0]] = 1
    for k, v in occurrences.items():
        if v == 2:
            corners.append(k)
    return corners


if __name__ == '__main__':
    ids, tiles = parse_tiles('input20.txt')
    joined_pairs = join_tiles(tiles,ids)
    corners = get_corners_ids(joined_pairs)
    corners_multiplied = functools.reduce(lambda a, b: a * b, corners)
    # ordered_ids = get_ordered_edges(joined_pairs,corners)
    print(corners_multiplied)
    print(corners)
    pprint(joined_pairs)
    print(len(joined_pairs))
    # print(ordered_ids)
