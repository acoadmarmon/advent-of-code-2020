import numpy as np

f = open('input.txt', 'r')
input_text = [val.split('\n')[0] for val in f.readlines()]
def get_front(lo, hi):
    return (lo, hi - int((hi - lo + 1)/2))

def get_back(lo, hi):
    return (lo + int((hi - lo + 1)/2), hi)

def get_seat_row_col(seat_str):
    lo, hi = (0, 127)
    row = -1
    col = -1
    for char in list(seat_str)[:7]:
        lo, hi = get_front(lo, hi) if char == 'F' else get_back(lo, hi)
    
    if lo == hi:
        row = lo
    else:
        print('Error, lo not equal to hi', lo, hi)
    
    lo, hi = (0, 7)
    for char in list(seat_str)[7:]:
        lo, hi = get_front(lo, hi) if char == 'L' else get_back(lo, hi)
    
    if lo == hi:
        col = lo
    else:
        print('Error, lo not equal to hi for col', lo, hi)
    
    return (row, col)


def part_1(input_text):
    row_cols = [get_seat_row_col(i) for i in input_text]
    return max([i[0]*8 + i[1] for i in row_cols])

print(part_1(input_text))

def part_2(input_text):
    row_cols = [get_seat_row_col(i) for i in input_text]
    possible_row_cols = []
    for i in range(128):
        for j in range(8):
            possible_row_cols.append((i, j))

    vals = [i[0]*8 + i[1] for i in row_cols]
    
    ids = []
    for i in possible_row_cols:
        if i not in row_cols:
            ids.append(i)
    return ids

print(part_2(input_text))
print(72*8 + 7)