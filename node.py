from puzzle import Puzzle

class Node():
    def __init__(self, puzzle: Puzzle, parent = None, action = None, heuristic = 1, cost = 1) -> None:
        self.puzzle = puzzle
        self.parent: Node = parent
        self.g = self.parent.g + cost if self.parent is not None else 0
        self.action = action
        self.f = self.calc_f()
        self.state = self._state()

    def calc_f(self, n = 1):
        return self.g + self.puzzle.heristic(n)

    def get_path(self):
        node, p = self, []
        while node:
            p.append(node)
            node = node.get_parent()
        yield from reversed(p)

    def get_actions(self):
        return self.puzzle.get_actions()

    def is_solved(self):
        return self.puzzle.is_solved()

    def get_parent(self):
        return self.parent

    def _state(self):
        return self.puzzle.get_state()
    
    def __str__(self):
        return self.puzzle.__str__()