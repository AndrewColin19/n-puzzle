import math

def manhattan(size: int, candidate: list[int], solved: list[int]):
    h = 0
    for i in range(size * size):
        if candidate[i] != 0 and candidate[i] != solved[i]:
            ci = solved.index(candidate[i])
            y = (i // size) - (ci // size)
            x = (i % size) - (ci % size)
            h += abs(y) + abs(x)
    return h // 2

def hamming(size: int, candidate: list[int], solved: list[int]):
    h = 0
    for i in range(size * size):
        if candidate[i] != 0 and candidate[i] != solved[i]:
            h += 1
    return h

def linear_conflicts(size, candidate:list[int], solved: list[int]):
    h = 0
    for i in range(size * size):
        if candidate[i] != 0 and candidate[i] != solved[i]:
            ci = solved.index(candidate[i])
            y = (i // size) - (ci // size)
            x = (i % size) - (ci % size)
            h += math.sqrt(abs(y) * abs(y) + abs(x) * abs(x))
    return h // 2