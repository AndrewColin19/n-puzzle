class Puzzle():
    def __init__(self, board: list[list], solution = None) -> None:
        self.board = board
        self.height = len(board)
        self.width = len(board[0])
        if solution is not None:
            self.solution = solution
        else:
            self.solution = self.get_final_step()

    def get_final_step(self):
        goal = [[0] * self.width for _ in range(self.height)]
        n = 1
        m = self.width * self.height
        for i in range(self.height):
            for j in range(self.width):
                if n == m:
                    n = 0
                goal[i][j] = n
                n += 1
        return goal
    
    def get_tiles_missplaced(self):
        h = 0
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] != self.solution[i][j]:
                    h += 1
        return h
    
    def is_solved(self):
        return False if self.get_tiles_missplaced() != 0 else True
    
    def get_copy(self):
        board = []
        for row in self.board:
            board.append([x for x in row])
        return board
    
    def _get_coord_zero(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == 0:
                    return y, x
    
    def get_actions(self):
        def create(at, to, action):
            return lambda: self.move(at, to, action)
        moves = []
        y, x = self._get_coord_zero()
        direcs = {'U': (y - 1, x), 
                  'D': (y + 1, x),
                  'R': (y, x + 1), 
                  'L': (y, x - 1)}
        for action, (r, c) in direcs.items():
            if self.board[y][x] == 0:
                if r >= 0 and c >= 0 and r < self.height and c < self.width:
                    move = create((y, x), (r, c), action), action
                    moves.append(move)
        return moves
    
    def move(self, at: tuple[int, int], to: tuple[int, int], action):
        at_y, at_x = at
        to_y, to_x = to
        copy = self.get_copy()
        copy[at_y][at_x], copy[to_y][to_x] = copy[to_y][to_x], copy[at_y][at_x]
        return Puzzle(copy)
    
    def get_state(self):
        return str(self.board)

    def __str__(self) -> str:
        m = (self.width * self.height) + (2 * self.width)
        s = ("-" * m) + "\n"
        for l in self.board:
            for c in l:
                s += f"| {c} |"
            s += "\n"
        s += ("-" * m) + "\n"
        return s