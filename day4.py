import regex as re


def get_list(file):
    with open(file) as f:
        lines = [line.strip() for line in f]
    return lines


def divide_passwords(l: [str]) -> [str]:
    passwords = []
    temp = ''
    for i in l:
        if i != '':
            temp = temp + ' ' + i
        elif i == '':
            passwords.append(temp.strip())
            temp = ''
    passwords.append(temp.strip())
    return passwords


def get_dict(password_data: str) -> dict:
    passw = password_data.split()
    password_dict = {}
    for passw_field in passw:
        k = passw_field[:3]
        v = passw_field[4:]
        password_dict[k] = v
    return password_dict


def check_fields(pass_data: dict, necessary: tuple) -> bool:
    for n in necessary:
        if n not in pass_data.keys():
            return False
    return True


def check_values(pass_data: dict) -> bool:
    necessary = (
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
    )
    if check_fields(pass_data, necessary):
        if check_byr(pass_data['byr']):
            if check_iyr(pass_data['iyr']):
                if check_eyr(pass_data['eyr']):
                    if check_hgt(pass_data['hgt']):
                        if check_hcl(pass_data['hcl']):
                            if check_ecl(pass_data['ecl']):
                                if check_pid(pass_data['pid']):
                                    return True
    return False


def check_byr(s: str):
    if s[0:2] == '19':
        if bool(re.match(r'[2-9][0-9]', s[2:4])):
            return True
    elif s[0:3] == '200':
        if s[3] in '012':
            return True
    return False


def check_iyr(s):
    if s[0:2] == '20':
        if re.match(r'1[0-9]', s[2:4]):
            return True
        elif s[2:] == '20':
            return True
    return False


def check_eyr(s):
    if s[0:2] == '20':
        if re.match(r'2[0-9]', s[2:4]):
            return True
        elif s[2:] == '30':
            return True
    return False


def check_hgt(s):
    if s[-2:] == 'cm' and len(s) == 5:
        if s[0] == '1':
            if re.match(r'[5-8][0-9]', s[1:3]):
                return True
            elif s[1] == '9' and re.match(r'[0-3]', s[2]):
                return True
    elif s[-2:] == 'in':
        if re.match(r'[5-6][0-9]', s[0:2]):
            return True
        elif s[0] == '7' and re.match(r'[0-6]', s[1]):
            return True
    return False


def check_hcl(s):
    if re.match(r'#[a-f0-9]{6}', s):
        return True
    return False


def check_ecl(s):
    if re.match(r'amb|blu|brn|gry|grn|hzl|oth', s):
        return True
    return False


def check_pid(s):
    if len(s) == 9 and re.match(r'[0-9]{9}', s):
        return True
    return False


if __name__ == '__main__':
    l = get_list('input4.txt')
    print(l)
    passwords = divide_passwords(l)
    print(passwords)
    data = []
    for i in passwords:
        data.append(get_dict(i))
    print(data)
    necessary_fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    validity = []
    for d in data:
        validity.append(check_fields(d, necessary_fields))
    print(validity)
    print(len(validity), sum(validity))

    values_validity = []
    for d in data:
        values_validity.append(check_values(d))
    print(values_validity)
    print(len(values_validity), sum(values_validity))
