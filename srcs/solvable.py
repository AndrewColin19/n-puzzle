import math

def count_inversions(puzzle):
    inversions = 0
    for i in range(len(puzzle)):
        for j in range(i + 1, len(puzzle)):
            if puzzle[i] > puzzle[j] != 0:
                inversions += 1
    return inversions

def find_blank_position(puzzle, size):
    blank_index = puzzle.index(0)
    blank_row = blank_index // size
    return size - blank_row

def is_solvable(puzzle, size):
    inversions = count_inversions(puzzle)
    blank_position = find_blank_position(puzzle, size)
    
    if size % 2 == 1:
        return inversions % 2 == 0
    else:
        return not ((inversions + blank_position) % 2 == 1)