"""
https://adventofcode.com/2020/day/14
"""
import re
from day4 import get_list


def get_parsed_input(file_name):
    l = get_list(file_name)
    mask_mem_items = []
    for i in l:
        if i[:2] == 'ma':
            mask = re.search(r'[X01]{36}', i).group()
            mask_mem_items.append([mask])
        else:
            mem_pair = [int(n) for n in re.findall(r'[0-9]+', i)]
            mask_mem_items[-1].append(mem_pair)
    return mask_mem_items


def get_binary(decimal_num: int) -> str:
    res = '0' * 36
    quotient = decimal_num
    i = len(res) - 1
    while quotient != 0:
        quotient, reminer = quotient // 2, quotient % 2
        res = res[:i] + str(reminer) + res[i + 1:]
        i -= 1
    return res


def get_decimal(binary_num: str) -> int:
    dec = 0
    for i in range(len(binary_num)):
        if binary_num[len(binary_num) - 1 - i] == '1':
            dec += 2 ** i
    return dec


def apply_mask(mask: str, binary_value: str) -> str:
    return ''.join([binary_value[i] if mask[i] == 'X' else mask[i] for i in range(len(binary_value))])


def save_mem(mask: str, mem_pair: [int, int], mem_dict) -> {}:
    mem_ind, binary_val = mem_pair[0], get_binary(mem_pair[1])
    mask_applied = get_decimal(apply_mask(mask, binary_val))
    mem_dict[mem_ind] = mask_applied
    return mem_dict


def decode_memory_address(mask: str, address_decimal: int) -> str:
    address = get_binary(address_decimal)
    new_address = ''
    for i in range(len(mask)):
        if mask[i] == '0':
            new_address += address[i]
        elif mask[i] == '1':
            new_address += '1'
        else:
            new_address += 'X'
    return new_address


def get_floating_possibilities(address: str) -> list:
    if 'X' not in address:
        return [address]
    possibilities = [address]
    res = []
    for i in range(len(address)):
        if address[i] == 'X':
            to_add = []
            for possible in possibilities:
                address1, address2 = possible[:i] + '0' + possible[i + 1:], possible[:i] + '1' + possible[i + 1:]
                to_add.extend([address1, address2])
            possibilities.extend(to_add)
    for possible in possibilities:
        if 'X' not in possible:
            res.append(get_decimal(possible))
    return res


def initialize(data: [[str, [int, int]]]) -> dict:
    memory = {}
    for item in data:
        mask, mem_val_pairs = item[0], item[1:]
        for pair in mem_val_pairs:
            memory = save_mem(mask, pair, memory)
    return memory


def initialize2(data: [[str, [int, int]]]) -> dict:
    memory = {}
    for item in data:
        mask, mem_val_pairs = item[0], item[1:]
        for address, value in mem_val_pairs:
            floating_address = decode_memory_address(mask, address)
            addresses = get_floating_possibilities(floating_address)
            for new_address in addresses:
                memory[new_address] = value
    return memory


if __name__ == '__main__':
    items = get_parsed_input('input14.txt')
    memory = initialize(items)  # part 1 solution
    print(sum(memory.values()))
    memory2 = initialize2(items)  # part 2 solution
    print(sum(memory2.values()))
