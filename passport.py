import numpy as np
from collections import defaultdict

def read_passport_list(input_lines):
    prev_pointer = 0
    new_list = []
    for i, val in enumerate(input_lines):
        if val == '':
            new_list.append(' '.join(input_lines[prev_pointer:i]))
            prev_pointer = i + 1

    new_list.append(' '.join(input_lines[prev_pointer:len(input_lines)]))

    all_passports = []
    for val in new_list:
        passport_dict = {i.split(':')[0]:i.split(':')[1] for i in val.split(' ')}
        passport_dict = defaultdict(str, passport_dict)
        passport = Passport(passport_dict)
        all_passports.append(passport)

    return all_passports

class Passport:
    def __init__(self, passport_dict):
        required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        self.all_fields_valid = all([i in passport_dict.keys() for i in required_fields]) and self.fields_valid(passport_dict)
        self.byr = passport_dict['byr']
        self.iyr = passport_dict['iyr']
        self.eyr = passport_dict['eyr']
        self.hgt = passport_dict['hgt']
        self.hcl = passport_dict['hcl']
        self.ecl = passport_dict['ecl']
        self.pid = passport_dict['pid']
        self.cid = passport_dict['cid']
    
    def fields_valid(self, passport_dict):
        # Check years are valid
        valid = int(passport_dict['byr']) >= 1920 and int(passport_dict['byr']) <= 2002 and \
               int(passport_dict['iyr']) >= 2010 and int(passport_dict['iyr']) <= 2020 and \
               int(passport_dict['eyr']) >= 2020 and int(passport_dict['eyr']) <= 2030 

        #Check height is valid
        is_cm = passport_dict['hgt'][-2:] == 'cm'
        if is_cm:

            valid = valid and int(passport_dict['hgt'][:-2]) >= 150 and int(passport_dict['hgt'][:-2]) <= 193
        else:
            valid = valid and  int(passport_dict['hgt'][:-2]) >= 59 and int(passport_dict['hgt'][:-2]) <= 76
        
        #Check hair color is valid
        valid = valid and passport_dict['hcl'][0] == '#'
        valid = valid and len(passport_dict['hcl']) == 7
        for i in list(passport_dict['hcl'][1:]):
            valid = valid and (i in ['0', '1', '2', '3','4', '5', '6', '7', '8', '9'] or i in ['a', 'b', 'c', 'd', 'e', 'f'])
        
        #Check eye color is valid
        valid = valid and passport_dict['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

        #Check pid is valid
        valid = valid and len(passport_dict['pid']) == 9
        for i in list(passport_dict['pid']):
            valid = valid and (i in ['0', '1', '2', '3','4', '5', '6', '7', '8', '9'])
        
        return valid

    
if __name__ == '__main__':
    f = open('./day-4/input.txt', 'r')
    input_text = [val.split('\n')[0] for val in f.readlines()]
    passports = read_passport_list(input_text)

    print('Part 2 is {}'.format(len([i for i in passports if i.all_fields_valid])))