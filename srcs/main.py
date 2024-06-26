from solver import Solver
from puzzle import Puzzle
from gen_puzzle import gen_puzzle
from argparse import ArgumentParser
from puzzle_parser import puzzle_parser
from heristic import heristics
from solvable import is_solvable

def main():
    parser = ArgumentParser()
    parser.add_argument("-s", "--size", type=int, help="Size of the puzzle's side. Must be >3.")
    parser.add_argument("-p", "--path", type=str, help="Path file of puzzle")
    parser.add_argument("-a", "--algo", type=int, default=4, help="Select heristic algo 1: manhattan, 2: hamming, 3: linear_conflicts, 4: all / Default: 4")
    args = parser.parse_args()
    if args.size and args.path:
        raise Exception("You cant have size and path.")
    if args.size and args.size < 3:
        raise Exception("Size must be sup or egal to 3.")
    if args.algo <= 0 and args.algo >= 4:
        raise Exception("Heristic must be in 1 and 3.")
    size, puzzle = puzzle_parser(args.path) if args.path else gen_puzzle(args.size if args.size else 3)
    if is_solvable(puzzle, size):
        raise Exception("Puzzle is not solvable.")
    solver = Solver(Puzzle(size, puzzle), heristic=heristics[args.algo])
    print("Solving...")
    paths, ct, cs, t = solver.solve()
    s = ""
    while s != "y" and s != "n":
        s = input("Do you want to see the solution? (y/n): ")
    if s == "y":
        solver.show_result(paths)
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