from heristic import manhattan

class Puzzle():
    def __init__(self, size: int, board: list[int], solution: list = None, heristic = manhattan) -> None:
        self.board: list[int] = board
        self.size: int = size
        if solution is not None:
            self.solution: list[int] = solution
        else:
            self.solution: list[int] = self.get_final_step()
        self._f_heristic = heristic
        self.solved = self._solved()

    def get_final_step(self):
        ts = self.size * self.size
        goal = [-1 for _ in range(ts)]
        cur = 1
        x = 0
        ix = 1
        y = 0
        iy = 0
        while True:
            goal[x + y*self.size] = cur
            if cur == 0:
                break
            cur += 1
            if x + ix == self.size or x + ix < 0 or (ix != 0 and goal[x + ix + y*self.size] != -1):
                iy = ix
                ix = 0
            elif y + iy == self.size or y + iy < 0 or (iy != 0 and goal[x + (y+iy)*self.size] != -1):
                ix = -iy
                iy = 0
            x += ix
            y += iy
            if cur == ts:
                cur = 0
        return goal
    
    def heristic(self):
        return self._f_heristic(self.size, self.board, self.solution)
    
    def _solved(self):
        for i in range(self.size * self.size):
            if self.board[i] != self.solution[i]:
                return False
        return True
    
    def get_copy(self):
        return [x for x in self.board]
    
    def get_actions(self):
        def create(at, to):
            return lambda: self.move(at, to)
        moves = []
        i = self.board.index(0)
        m = [i + 1, i - 1, i + self.size, i - self.size]
        for x, y in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            x = i % self.size + x 
            y = i // self.size + y 
            if x >= self.size or x < 0 or y < 0 or y >= self.size:
                continue
            move = create(i, y * self.size + x)
            moves.append(move)
        return moves
    
    def move(self, at: int, to: int):
        copy = self.get_copy()
        copy[at], copy[to] = copy[to], copy[at]
        return Puzzle(self.size, copy, self.solution)