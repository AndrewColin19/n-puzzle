import random

def make_goal(size):
    ts = size*size
    goal = [-1 for _ in range(ts)]
    cur = 1
    x = 0
    ix = 1
    y = 0
    iy = 0
    while True:
        goal[x + y*size] = cur
        if cur == 0:
            break
        cur += 1
        if x + ix == size or x + ix < 0 or (ix != 0 and goal[x + ix + y * size] != -1):
            iy = ix
            ix = 0
        elif y + iy == size or y + iy < 0 or (iy != 0 and goal[x + (y + iy) * size] != -1):
            ix = -iy
            iy = 0
        x += ix
        y += iy
        if cur == ts:
            cur = 0
    return goal

def gen_puzzle(size: int, solvable: bool = True) -> tuple[int, list]:
    def swap_empty(p: list):
        idx = p.index(0)
        poss = []
        if idx % size > 0:
            poss.append(idx - 1)
        if idx % size < size - 1:
            poss.append(idx + 1)
        if idx / size > 0 and idx - size >= 0:
            poss.append(idx - size)
        if idx / size < size - 1:
            poss.append(idx + size)
        swi = random.choice(poss)
        p[idx] = p[swi]
        p[swi] = 0
        return p
    if solvable:
        print(f"Generate solvable puzzle size: {size}")
    else:
        print(f"Generate unsolvable puzzle size: {size}")
    l = make_goal(size)
    for _ in range(1000):
        l = swap_empty(l)
    if not solvable:
        if l[0] == 0 or l[1] == 0:
            l[-1], l[-2] = l[-2], l[-1]
        else:
            l[0], l[1] = l[1], l[0]
    return size, l