"""
https://adventofcode.com/2020/day/18
"""
import re
from day4 import get_list


def do_basic_operation(exp: str):
    operators = re.findall(r'[+*]', exp)
    nums = [int(n) for n in re.findall(r'\d+', exp)]
    r = nums[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            r += nums[i + 1]
        else:
            r *= nums[i + 1]
    return r


def calculate(expression: str) -> int:
    exp = expression.replace(' ', '')
    ind_open_parenthesis = list(filter(lambda p: exp[p] == '(', range(len(exp))))
    ind_close_parenthesis = list(filter(lambda p: exp[p] == ')', range(len(exp))))
    opened, closed = 0, 0
    initial_len = len(exp)
    temp_opened_ind, temp_closed_ind = [], []
    for parenthesis in sorted(ind_open_parenthesis + ind_close_parenthesis):
        len_refactor = initial_len - len(exp)
        if exp[parenthesis - len_refactor] == '(':
            opened += 1
            temp_opened_ind.append(parenthesis - len_refactor)
        elif exp[parenthesis - len_refactor] == ')':
            closed += 1
            temp_closed_ind.append(parenthesis - len_refactor)
        if closed != 0:
            opened -= 1
            closed -= 1
            inner_exp = exp[temp_opened_ind[-1] + 1:temp_closed_ind[0]]
            exp = exp[:temp_opened_ind[-1]] + str(do_basic_operation(inner_exp)) + exp[temp_closed_ind[0] + 1:]
            temp_opened_ind, temp_closed_ind = temp_opened_ind[:-1], temp_closed_ind[1:]
    return do_basic_operation(exp)


def add_addition_priority(expression: str) -> str:
    exp = expression.replace(' ', '')
    pluses_num = exp.count('+')
    for p in range(pluses_num):
        pluses_ind = [ind for ind in range(len(exp)) if exp[ind] == '+']
        current_ind = pluses_ind[p]
        left, right = False, False
        left_ind, right_ind = current_ind - 1, current_ind + 1
        par_opened, par_closed = 0, 0
        while not left:
            if left_ind == 0 or (par_opened == par_closed and exp[left_ind - 1] in '(+*'):
                left = True
            elif exp[left_ind - 1] == '(':
                par_opened += 1
                left_ind -= 1
            elif exp[left_ind] == ')':
                par_closed += 1
                left_ind -= 1
            else:
                left_ind -= 1
        while not right:
            if right_ind + 1 == len(exp) or (par_opened == par_closed and exp[right_ind + 1] in ')+*'):
                right = True
            elif exp[right_ind] == '(':
                par_opened += 1
                right_ind += 1
            elif exp[right_ind + 1] == ')':
                par_closed += 1
                right_ind += 1
            else:
                right_ind += 1
        exp = exp[:left_ind] + '(' + exp[left_ind:right_ind + 1] + ')' + exp[right_ind + 1:]
    return exp


if __name__ == '__main__':
    operations = get_list('input18.txt')
    part1_operations = sum([calculate(expression) for expression in operations])
    operations_plus_priority = [add_addition_priority(exp) for exp in operations]
    part2_operations = sum([calculate(expression) for expression in operations_plus_priority])
    print(part1_operations, part2_operations)
