import numpy as np

f = open('input.txt', 'r')
input_text = [val.split('\n')[0] for val in f.readlines()]


prev_pointer = 0
new_list = []
for i, val in enumerate(input_text):
    if val == '':
        new_list.append(' '.join(input_text[prev_pointer:i]))
        prev_pointer = i + 1

new_list.append(' '.join(input_text[prev_pointer:len(input_text)]))
    
def part_1():
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    num_valid = 0
    for val in new_list:
        passport_dict = {i.split(':')[0]:i.split(':')[1] for i in val.split(' ')}
        is_valid = all([i in passport_dict.keys() for i in required_fields])
        if is_valid:
            num_valid = num_valid + 1
    return num_valid

print(part_1())

def part_2():
    def valid_passport(pass_dict):
        valid = int(pass_dict['byr']) >= 1920 and int(pass_dict['byr']) <= 2002 and \
               int(pass_dict['iyr']) >= 2010 and int(pass_dict['iyr']) <= 2020 and \
               int(pass_dict['eyr']) >= 2020 and int(pass_dict['eyr']) <= 2030 

        is_cm = pass_dict['hgt'][-2:] == 'cm'
        if is_cm:

            valid = valid and int(pass_dict['hgt'][:-2]) >= 150 and int(pass_dict['hgt'][:-2]) <= 193
        else:
            valid = valid and  int(pass_dict['hgt'][:-2]) >= 59 and int(pass_dict['hgt'][:-2]) <= 76
        
        valid = valid and pass_dict['hcl'][0] == '#'
        valid = valid and len(passport_dict['hcl']) == 7
        for i in list(pass_dict['hcl'][1:]):
            valid = valid and (i in ['0', '1', '2', '3','4', '5', '6', '7', '8', '9'] or i in ['a', 'b', 'c', 'd', 'e', 'f'])
        
        valid = valid and pass_dict['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        valid = valid and len(pass_dict['pid']) == 9
        for i in list(pass_dict['pid']):
            valid = valid and (i in ['0', '1', '2', '3','4', '5', '6', '7', '8', '9'])
        
        return valid

    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    num_valid = 0
    for val in new_list:
        passport_dict = {i.split(':')[0]:i.split(':')[1] for i in val.split(' ')}
        is_valid = all([i in passport_dict.keys() for i in required_fields]) and valid_passport(passport_dict)

        if is_valid:
            num_valid = num_valid + 1
    return num_valid

print(part_2())