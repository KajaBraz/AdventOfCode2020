from day4 import get_list


def parse_instr(instructions: [str]) -> list:
    parsed = []
    for i in instructions:
        parsed.append((i[:3], i[4], int(i[5:])))
    return parsed


def implement_rules(instruction: str, operator: str, value: int, n: int, ind: int) -> (int, int):
    if operator == '-':
        value *= -1
    if instruction == 'acc':
        return n + value, ind + 1
    elif instruction == 'jmp':
        return n, ind + value
    elif instruction == 'nop':
        return n, ind + 1


def run_boot_code(instructions: [(str, str, int)]) -> int:
    bool_list = [True] * len(instructions)
    res, ind = 0, 0
    while bool_list[ind]:
        bool_list[ind] = False
        res, ind = implement_rules(instructions[ind][0], instructions[ind][1], instructions[ind][2], res, ind)
    return res


def fix_boot_code(instructions: [(str, str, int)]):
    res, ind = 0, 0
    bool_list = [True] * len(instructions)
    fixed = False
    changes = {'jmp': 'nop', 'nop': 'jmp'}
    potential_changes = [i for i in range(len(instructions)) if instructions[i][0] in changes.keys()]
    potential_change_ind = -1
    instructions_copy = instructions[:]
    while not fixed:
        while ind < len(bool_list) and bool_list[ind]:
            bool_list[ind] = False
            res, ind = implement_rules(instructions_copy[ind][0], instructions_copy[ind][1], instructions_copy[ind][2],
                                       res, ind)
        if ind == len(instructions_copy):
            fixed = True
        else:
            if potential_change_ind < len(potential_changes) - 1:
                potential_change_ind += 1
                fix_ind = potential_changes[potential_change_ind]
                instructions_copy = instructions[:]
                instructions_copy[fix_ind] = (
                    changes[instructions[fix_ind][0]], instructions[fix_ind][1], instructions[fix_ind][2])
                res, ind = 0, 0
                bool_list = [True] * len(instructions)
            else:
                fixed = True
    return res


if __name__ == '__main__':
    instruction_list = get_list('input8.txt')
    print(instruction_list)
    instruction_list_parsed = parse_instr(instruction_list)
    print(instruction_list_parsed)
    value_before_repetition = run_boot_code(instruction_list_parsed)
    print(value_before_repetition)
    fixed_res = fix_boot_code(instruction_list_parsed)
    print(fixed_res)
