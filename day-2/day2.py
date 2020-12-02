import numpy as np

f = open('input.txt', 'r')
input_text = [val.split('\n')[0] for val in f.readlines()]

inputs = np.asarray([i.split(':') for i in input_text])

def part_1(problem):
    vals = [(i[0].split(' ')[0], i[0].split(' ')[1], i[1][1:]) for i in problem]
    min_max = [((int(i[0].split('-')[0]), int(i[0].split('-')[1])), i[1], i[2]) for i in vals]

    counter = 0
    for extrema, val, password in min_max:
        min_val, max_val = extrema
        num_val = len([i for i in password if i == val])
        if num_val >= min_val and num_val <= max_val:
            counter = counter + 1
    return counter

def part_2(problem):
    vals = [(i[0].split(' ')[0], i[0].split(' ')[1], i[1][1:]) for i in problem]
    min_max = [((int(i[0].split('-')[0]), int(i[0].split('-')[1])), i[1], i[2]) for i in vals]

    counter = 0
    for extrema, val, password in min_max:
        min_val, max_val = extrema
        min_val = min_val - 1
        max_val = max_val - 1
        is_min = password[min_val] == val
        is_max = password[max_val] == val

        if bool(is_min) != bool(is_max):
            counter = counter + 1    


    return counter

print(part_1(inputs))
print(part_2(inputs))