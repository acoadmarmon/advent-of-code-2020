import numpy as np

f = open('input.txt', 'r')
input_text = [val.split('\n')[0] for val in f.readlines()]

print(input_text)

input_array = np.asarray([int(i) for i in input_text])

# Part 1
for idx, i in enumerate(input_array):
    for jdx, j in enumerate(input_array):
        if idx != jdx:
            if i + j == 2020:
                print(input_array[idx]*input_array[jdx])
                #exit(0)

# Part 2
for idx, i in enumerate(input_array):
    for jdx, j in enumerate(input_array):
        for kdx, k in enumerate(input_array):
            if idx != jdx and idx != kdx:
                if i + j + k == 2020:
                    print(input_array[idx]*input_array[jdx]*input_array[kdx])
                    exit(0)