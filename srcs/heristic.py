import math

# def manhattan(size: int, candidate: list[int], solved: list[int]):
#     h = 0
#     for i in range(size * size):
#         if candidate[i] != 0 and candidate[i] != solved[i]:
#             ci = solved.index(candidate[i])
#             y = (i // size) - (ci // size)
#             x = (i % size) - (ci % size)
#             h += abs(y) + abs(x)
#     return h // 2

def manhattan(size: int, grid: list[int], goal: list[int]) -> int:
	res = 0
	coords = {e: (i // size, i % size) for i, e in enumerate(goal)}
	for i, e in enumerate(grid):
		cury = i // size
		curx = i % size
		targety, targetx = coords[e]
		res += abs(curx - targetx) + abs(cury - targety)
	return res

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

# TODO May not be admissible
def squared(size: int, grid: list[int], goal: list[int]) -> int:
	res = 0
	coords = {e: (i // size, i % size) for i, e in enumerate(goal)}
	for i, e in enumerate(grid):
		cury = i // size
		curx = i % size
		targety, targetx = coords[e]
		res += (curx - targetx)**2 + (cury - targety)**2
	return res

# TODO May not be admissible
def misplaced(size: int, grid: list[int], goal: list[int]) -> int:
	return sum(a != b for a, b in zip(grid, goal))


heristics = {
    1: manhattan,
    2: hamming,
    3: linear_conflicts,
    4: squared,
    5: misplaced
}