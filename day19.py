"""
https://adventofcode.com/2020/day/19
"""
from day4 import get_list
import re


def get_rules(file) -> dict:
    rules_list = get_list(file)
    rules = {rule_num: ' ' + val + ' ' for (rule_num, val) in [rule.split(':') for rule in rules_list]}
    return rules


def define_rule_0(rules: {str: str}) -> str:
    zero = rules['0']
    defined = zero[:]
    while re.search(r'\d', defined):
        numbers = re.findall(r'\d+', defined)
        for number in numbers:
            replacer = ' ( ' + rules[number] + ' ) '
            defined = re.sub(' ' + number + ' ', replacer, defined)
    return defined


def check(rule: str, messages: [str]) -> int:
    rule = re.sub(r'[\s"]', '', rule)
    rule = '^' + rule + '$'
    correct = [True for message in messages if re.search(rule, message)]
    return sum(correct)


if __name__ == '__main__':
    messages = get_list('input19_messages.txt')
    rules = get_rules('input19_rules.txt')
    print(check(define_rule_0(rules), messages))  # part 1 solution
    rules2 = dict(rules)
    rules2['8'] = '( 42 )+'
    rules2['11'] = ' 42 31 | 42 42 31 31 | 42 42 42 31 31 31 | 42 42 42 42 31 31 31 31 | 42 42 42 42 42 31 31 31 31 31 '
    print(check(define_rule_0(rules2), messages))  # part 2 solution
