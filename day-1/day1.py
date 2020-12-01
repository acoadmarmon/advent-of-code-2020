import numpy as np

f = open('input.txt', 'r')
input_text = [val.split('\n')[0] for val in f.readlines()]

input_array = np.asarray([int(i) for i in input_text])

def part_1():
    for idx, i in enumerate(input_array):
        for jdx, j in enumerate(input_array):
            if idx != jdx:
                if i + j == 2020:
                    return i*j

def part_2():
    for idx, i in enumerate(input_array):
        for jdx, j in enumerate(input_array):
            for kdx, k in enumerate(input_array):
                if idx != jdx and idx != kdx:
                    if i + j + k == 2020:
                        return i*j*k


print('Part 1 answer is {}'.format(part_1()))
print('Part 2 answer is {}'.format(part_2()))