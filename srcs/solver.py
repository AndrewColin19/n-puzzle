import time
import heapq
import os
from puzzle import Puzzle

class Solver():
    def __init__(self, puzzle: Puzzle, heristic, cost: int = 1) -> None:
        self.puzzle = tuple(puzzle.board)
        self._puzzle_size = puzzle.size
        self._goal = puzzle.goal
        self._heristic = heristic
        self._cost = cost

    def _is_solved(self, current):
        for i in range(self._puzzle_size * self._puzzle_size):
            if current[i] != self._goal[i]:
                return False
        return True

    def _get_neighbors(self, current):
        neighbors = []
        zero_index = current.index(0)
        zero_row, zero_col = divmod(zero_index, self._puzzle_size)
        
        def swap_and_clone(a, b):
            new_puzzle = list(current)
            new_puzzle[a], new_puzzle[b] = new_puzzle[b], new_puzzle[a]
            return tuple(new_puzzle)
        
        if zero_row > 0:
            neighbors.append(swap_and_clone(zero_index, zero_index - self._puzzle_size))
        if zero_row < self._puzzle_size - 1:
            neighbors.append(swap_and_clone(zero_index, zero_index + self._puzzle_size))
        if zero_col > 0:
            neighbors.append(swap_and_clone(zero_index, zero_index - 1))
        if zero_col < self._puzzle_size - 1:
            neighbors.append(swap_and_clone(zero_index, zero_index + 1))
        
        return neighbors

    def _reconstruct_path(self, came_from, current):
        path = [current]
        while hash(str(current)) in came_from:
            current = came_from[hash(str(current))]
            path.append(current)
        path.reverse()
        return path

    def _a_star(self):
        open_set = []
        heapq.heappush(open_set, (0, self.puzzle))
        came_from = {}
        g_score = {hash(str(self.puzzle)): 0}
        f_score = {hash(str(self.puzzle)): self._heristic(self._puzzle_size, self.puzzle, self._goal)}
        closed_set = set()
        start = time.time()
        while open_set:
            _, current = heapq.heappop(open_set)
            if self._is_solved(current):
                end = time.time() - start
                return self._reconstruct_path(came_from, current), len(open_set), len(closed_set), end
            closed_set.add(hash(str(current)))
            for neighbor in self._get_neighbors(current):
                h = hash(str(neighbor))
                if h in closed_set:
                    continue
                tentative_g_score = g_score[hash(str(current))] + 1
                if h not in g_score or tentative_g_score < g_score[h]:
                    came_from[h] = current
                    g_score[h] = tentative_g_score
                    f_score[h] = tentative_g_score + self._heristic(self._puzzle_size, neighbor, self._goal)
                    if h not in [i[1] for i in open_set]:
                        heapq.heappush(open_set, (f_score[h], neighbor))
    
    def solve(self):
        return self._a_star()
    
    def _format_node(self, path):
        f = "-" * 3 * self._puzzle_size + "\n"
        for _ in range(self._puzzle_size):
            f += "{:<3} " * self._puzzle_size + "\n"
        f += "-" * 3 * self._puzzle_size + "\n"
        return f.format(*path)
    
    def show_result(self, paths: list[tuple[int]]):
        def clear_console():
                os.system('cls') if os.name == 'nt' else os.system('clear')
        for path in paths:
            clear_console()
            print(self._format_node(path))
            time.sleep(0.5)
