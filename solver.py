class Puzzle():
    def __init__(self, board: list[list]) -> None:
        self.board = board
        self.y_size = len(board)
        self.x_size = len(board[0])

class Node():
    def __init__(self, puzzle: list[list], parent: Node = None, action = None) -> None:
        self._puzzle = puzzle
        self._parent: Node = parent
        self._action = action

    def path(self):
        node, p = self, []
        while node:
            p.append(node)
            node = node.get_parent()
        yield from reversed(p)

    def get_parent(self):
        return self._parent

class Solver():
    def __init__(self, puzzle: list[list]) -> None:
        self._direct = {'U':(1, 0), 'D':(-1, 0), 'L':(0, -1), 'R':(0, 1)}
        self.puzzle = puzzle
        self._y_size = len(puzzle)
        self._x_size = len(puzzle[0])
        self._goal = self._get_goal()
        self._h = self._get_tiles_missplaced()
        self._g = 0
        self._f = self._g + self._h #(x) = g(x)+h(X)
    
    def _get_goal(self):
        goal = [[0] * self._x_size for _ in range(self._y_size)]
        n = 1
        m = self._x_size * self._y_size
        for i in range(self._y_size):
            for j in range(self._x_size):
                if n == m:
                    n = 0
                goal[i][j] = n
                n += 1
        return goal
        
    def __str__(self) -> str:
        s = f"Puzzle: {self._x_size}*{self._y_size}\n"
        m = (self._x_size * self._y_size) + (2 * self._x_size)
        s += ("-" * m) + "\n"
        for l in self.puzzle:
            for c in l:
                s += f"| {c} |"
            s += "\n"
        s += ("-" * m) + "\n"
        s += f"Goal: {self._x_size}*{self._y_size}\n"
        s += ("-" * m) + "\n"
        for l in self._goal:
            for c in l:
                s += f"| {c} |"
            s += "\n"
        s += ("-" * m) + "\n"
        s += f"h: {self._h} g: {self._g} f: {self._f}\n"
        return s

    def _get_tiles_missplaced(self):
        h = 0
        for i in range(self._y_size):
            for j in range(self._x_size):
                if self.puzzle[i][j] != self._goal[i][j]:
                    h += 1
        return h
    
    def move(self, at: tuple[int, int], to: tuple[int, int]):
        at_y, at_x = at
        to_y, to_x = to
        copy = self.puzzle.copy()
        copy[at_y][at_x], copy[to_y][to_x] = copy[to_y][to_x], copy[at_y][at_x]
        return copy
            