import time
from solver import Solver
from puzzle import Puzzle


t = [[[0, 8, 5], [4, 1, 7], [2, 6, 3]], [[8, 0, 5], [4, 1, 7], [2, 6, 3]], [[8, 1, 5], [4, 0, 7], [2, 6, 3]], [[8, 1, 5], [4, 6, 7], [2, 0, 3]], [[8, 1, 5], [4, 6, 7], [2, 3, 0]], [[8, 1, 5], [4, 6, 0], [2, 3, 7]], [[8, 1, 5], [4, 0, 6], [2, 3, 7]], [[8, 1, 5], [4, 3, 6], [2, 0, 7]], [[8, 1, 5], [4, 3, 6], [0, 2, 7]], [[8, 1, 5], [0, 3, 6], [4, 2, 7]], [[0, 1, 5], [8, 3, 6], [4, 2, 7]], [[1, 0, 5], [8, 3, 6], [4, 2, 7]], [[1, 3, 5], [8, 0, 6], [4, 2, 7]], [[1, 3, 5], [8, 2, 6], [4, 0, 7]], [[1, 3, 5], [8, 2, 6], [4, 7, 0]], [[1, 3, 5], [8, 2, 0], [4, 7, 6]], [[1, 3, 0], [8, 2, 5], [4, 7, 6]], [[1, 0, 3], [8, 2, 5], [4, 7, 6]], [[1, 2, 3], [8, 0, 5], [4, 7, 6]], [[1, 2, 3], [0, 8, 5], [4, 7, 6]], [[1, 2, 3], [4, 8, 5], [0, 7, 6]], [[1, 2, 3], [4, 8, 5], [7, 0, 6]], [[1, 2, 3], [4, 0, 5], [7, 8, 6]], [[1, 2, 3], [4, 5, 0], [7, 8, 6]], [[1, 2, 3], [4, 5, 6], [7, 8, 0]]]

def str_n_puzzle(boards, width, height, n=5):
    st = ""
    for j in range(height):
        s = "| "
        for x in range(n):
            for i in range(width):
                s += str(boards[x][j][i])
                s += " " if i + 1 < width else ""
            s += " |   | " if x + 1 < n else " |\n"
        st += s
    return st

def print_paths(boards):
    for row in boards:
        print(row)

def main():
    puzzle = Puzzle([[0, 8, 5], [4, 1, 7], [2, 6, 3]])
    s = Solver(puzzle)
    start = time.time()
    paths, opened, closed = s.solve(2)
    end = time.time() - start
    boards = []
    for p in paths:
        boards.append(p.puzzle.board_row)
    print(f"Complexity in time: {len(opened)}")
    print(f"Complexity in size: {len(closed)}")
    print(f"Number of steps to solve: {len(boards)}")
    print_paths(boards)
    print(f"Solved in {round(end, 2)}s")

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("goodbye")
    except Exception as e:
        print(e)

    """
    TODO
    nb state never selected (complexity in time)
    nb state never selected in memory (complexity in size)
    nb move (ez)
    ordered seq (print_paths)
    
    unsovable puzzle
    """