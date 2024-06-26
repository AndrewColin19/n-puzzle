from solver import Solver
from puzzle import Puzzle
from node import Node
from gen_puzzle import gen_puzzle
from argparse import ArgumentParser
from puzzle_parser import puzzle_parser
from heristic import heristics
import os, time

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

def format_node(node: Node):
        f = "-" * 3 * node.size + "\n"
        for _ in range(node.size):
            f += "{:<3} " * node.size + "\n"
        f += "-" * 3 * node.size + "\n"
        return f.format(*node.puzzle.board)

def print_borads(boards: list[Node]):
    def clear_console():
            os.system('cls') if os.name == 'nt' else os.system('clear')
    for node in boards:
        clear_console()
        print(format_node(node))
        time.sleep(0.5)

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
    parser.add_argument("-s", "--size", type=int, help="Size of the puzzle's side. Must be >3.")
    parser.add_argument("-p", "--path", type=str, help="Path file of puzzle")
    parser.add_argument("-a", "--algo", type=int, default=1, help="Select heristic algo 1: manhattan, 2: hamming, 3: linear_conflicts")
    args = parser.parse_args()
    if args.size and args.path:
        raise Exception("You cant have size and path.")
    if args.size and args.size < 3:
        raise Exception("Size must be sup or egal to 3.")
    if args.algo <= 0 and args.algo >= 4:
        raise Exception("Heristic must be in 1 and 3.")
    size, puzzle = puzzle_parser(args.path) if args.path else gen_puzzle(args.size if args.size else 3)
    # if not is_solvable(puzzle):
    #     raise Exception("Puzzle is not solvable.")
    s = Solver(Puzzle(size, puzzle, heristic=heristics[args.algo]))
    paths, ct, cs, t = s.solve()
    input("Press Enter to see the solution")
    print_borads(paths)
    print(f"Complexity in time: {ct}")
    print(f"Complexity in size: {cs}")
    print(f"Number of steps to solve: {len(paths) - 1}")
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