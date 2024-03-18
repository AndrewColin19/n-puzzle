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

def print_paths(boards, width, height):
    size = len(boards)
    inc = 10
    print(end="\n\n")
    if size / inc < 1:
        print(str_n_puzzle(boards, width, height, size))
    else:
        i = 0
        while i != size:
            print(str_n_puzzle(boards, width, height, inc), end='')
            if i + inc >= size:
                inc = size - i
                i += size - i
            else:
                print(end='\n\n')
                i += inc

def main():
    puzzle = Puzzle([[0, 8, 5], [4, 1, 7], [2, 6, 3]])
    s = Solver(puzzle)
    paths = s.solve()
    
    board = []
    for p in paths:
        board.append(p.puzzle.board)
    print(f"Solved in {len(board)} steps")
    print_paths(board, 3, 3)

if __name__=='__main__':
    main()

    """
    TODO
    nb state never selected (complexity in time)
    nb state never selected in memory (complexity in size)
    nb move (ez)
    ordered seq (print_paths)
    
    unsovable puzzle
    """