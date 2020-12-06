from day4 import get_list, divide_passwords


def count_unique(s: str) -> int:
    unique = set(s)
    if ' ' in unique:
        unique.remove(' ')
    return len(unique)


def answered_by_all(s: str) -> int:
    qs = s.split()
    qs_sets = []
    for q in qs:
        qs_sets.append(set(q))
    qs_intersection = set.intersection(*qs_sets)
    return len(qs_intersection)


if __name__ == '__main__':
    l = get_list('input6.txt')
    print(l)
    group_qs = divide_passwords(l)
    print(group_qs)
    unique = []
    for i in group_qs:
        unique.append(count_unique(i))
    print(unique, '\n', sum(unique))
    everyone_answered = []
    for i in group_qs:
        everyone_answered.append(answered_by_all(i))
    print(everyone_answered, '\n', sum(everyone_answered))
