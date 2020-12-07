import numpy as np
from collections import Counter

f = open('input.txt', 'r')
input_text = [val.split('\n')[0] for val in f.readlines()]

prev_pointer = 0
new_list = []
for i, val in enumerate(input_text):
    if val == '':
        new_list.append(''.join(input_text[prev_pointer:i]))
        prev_pointer = i + 1

new_list.append(''.join(input_text[prev_pointer:len(input_text)]))

def part_1(list_of_groups):
    unique_answers = 0
    for i in list_of_groups:
        answer_counts = Counter(i)
        unique_answers = unique_answers + len(answer_counts.keys())
    return unique_answers

print(part_1(new_list))

prev_pointer = 0
new_list = []
for i, val in enumerate(input_text):
    if val == '':
        new_list.append(' '.join(input_text[prev_pointer:i]))
        prev_pointer = i + 1

new_list.append(' '.join(input_text[prev_pointer:len(input_text)]))

def part_2(list_of_groups):
    unique_answers = 0
    for i in list_of_groups:
        group_answers = i.split(' ')
        group_len = len(group_answers)

        group = ''.join(group_answers)
        answer_counts = Counter(group)

        unique_answers = unique_answers + len([k for k,v in answer_counts.items() if v == group_len])
    return unique_answers

print(part_2(new_list))