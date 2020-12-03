import numpy as np

f = open('input.txt', 'r')
input_text = [val.split('\n')[0] for val in f.readlines()]

matrix = np.asarray([list(val) for val in input_text])

def part_1():
    num_trees = 0
    curr_column = 0
    for i in range(matrix.shape[0]):
        if matrix[i][curr_column] == '#':
            num_trees = num_trees + 1

        curr_column = curr_column + 3
        if curr_column >= matrix.shape[1]:
            curr_column = curr_column - matrix.shape[1]
    return num_trees


def part_2(right, down):
    num_trees = 0
    curr_column = 0
    for i in range(0, matrix.shape[0], down):
        if matrix[i][curr_column] == '#':
            num_trees = num_trees + 1

        curr_column = curr_column + right
        if curr_column >= matrix.shape[1]:
            curr_column = curr_column - matrix.shape[1]
    return num_trees


ans = 1
for i in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    ans = ans*part_2(i[0], i[1])

print('Part one answer is {}'.format(part_1()))
print('Part two answer is {}'.format(ans))