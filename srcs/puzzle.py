class Puzzle():
    def __init__(self, size: int, board: tuple[int]) -> None:
        self.board: tuple[int] = board
        self.size: int = size
        self.goal: tuple[int] = self.get_goal()

    def get_goal(self):
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