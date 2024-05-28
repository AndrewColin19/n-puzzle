from solver import Solver
from puzzle import Puzzle
from gen_puzzle import gen_puzzle
from argparse import ArgumentParser
from puzzle_parser import parse_puzzle

def get_puzzle(path='puzzle'):
    t = []
    with open(path) as file:
        s = file.read()
        for row in s.split('\n'):
            r = []
            for n in row:
                r.append(int(n))
            t.append(r)
    return t

def print_std(boards):
    for node in boards:
        print(node)

def print_pretty(boards):
    for node in boards:
        print(node.pretty_str())

def is_solvable(puzzle):
    inversions = 0

    for i in range(len(puzzle)):
        for j in range(i + 1, len(puzzle)):
            if puzzle[j] > puzzle[i]:
                inversions += 1

    if inversions % 2 == 1:
        return False
    else:
        return True

def main():
    parser = ArgumentParser()
    parser.add_argument("-size", "--size", type=int, help="Size of the puzzle's side. Must be >3.")
    parser.add_argument("-path", "--path", type=str, help="Path file of puzzle")
    parser.add_argument("-heristic", "--heristic", type=int, default=1, help="Select heristic algo 1: manhattan, 2: hamming, 3: linear_conflicts")
    args = parser.parse_args()
    if args.size and args.path:
        raise Exception("You cant have size and path.")
    if args.size and args.size < 3:
        raise Exception("Size must be sup or egal to 3.")
    if args.heristic <= 0 and args.heristic >= 4:
        raise Exception("Heristic must be in 1 and 3.")
    size, puzzle = parse_puzzle(args.path) if args.path else gen_puzzle(args.size if args.size else 3)
    if not is_solvable(puzzle):
        raise Exception("Puzzle is not solvable.")
    s = Solver(Puzzle(size, puzzle))
    paths, ct, cs, t = s.solve(args.heristic)
    print(f"Complexity in time: {ct}")
    print(f"Complexity in size: {cs}")
    print(f"Number of steps to solve: {len(paths) - 1}")
    # print_std(paths)
    print_pretty(paths)
    print(f"Solved in {round(t, 4)}s")

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("goodbye")
    except FileNotFoundError as fe:
        print(f"{fe.filename} not found")
    except Exception as e:
        print(e)