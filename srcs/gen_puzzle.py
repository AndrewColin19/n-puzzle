import argparse
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

def gen_puzzle(size: int, solvable: bool = True, iteration: int = 100, p = True) -> tuple[int, list]:
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
        msg = f"Generate solvable puzzle size: {size}"
    else:
        msg = f"Generate unsolvable puzzle size: {size}"
    if p:
        print(msg)
    l = make_goal(size)
    for _ in range(iteration):
        l = swap_empty(l)
    if not solvable:
        if l[0] == 0 or l[1] == 0:
            l[-1], l[-2] = l[-2], l[-1]
        else:
            l[0], l[1] = l[1], l[0]
    return size, l


if __name__ == "__main__":
	parser = argparse.ArgumentParser()

	parser.add_argument("size", type=int, help="Size of the puzzle's side. Must be >3.")
	parser.add_argument("-s", "--solvable", action="store_true", default=False, help="Forces generation of a solvable puzzle. Overrides -u.")
	parser.add_argument("-u", "--unsolvable", action="store_true", default=False, help="Forces generation of an unsolvable puzzle")
	parser.add_argument("-i", "--iterations", type=int, default=100, help="Number of passes")

	args = parser.parse_args()

	random.seed()

	if args.solvable and args.unsolvable:
		print("Can't be both solvable AND unsolvable, dummy !")
		exit(1)

	if args.size < 3:
		print("Can't generate a puzzle with size lower than 2. It says so in the help. Dummy.")
		exit(0)

	if not args.solvable and not args.unsolvable:
		solv = random.choice([True, False])
	elif args.solvable:
		solv = True
	elif args.unsolvable:
		solv = False

	s = args.size
	s, puzzle = gen_puzzle(s, solv, iteration=args.iterations, p=False)

	w = len(str(s*s))
	print("# This puzzle is %s" % ("solvable" if solv else "unsolvable"))
	print("%d" % s)
	for y in range(s):
		for x in range(s):
			print("%s" % (str(puzzle[x + y * s]).rjust(w)), end=' ')
		print()