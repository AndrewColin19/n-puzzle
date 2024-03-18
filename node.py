from puzzle import Puzzle

class Node():
    def __init__(self, puzzle: Puzzle, parent = None, action = None, g = 1) -> None:
        self.puzzle = puzzle
        self.parent: Node = parent
        self.action = action
        self.f = self.calc_f(g)

    def calc_f(self, g = 1):
        return g + self.puzzle.get_tiles_missplaced()

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

    def state(self):
        return self.puzzle.get_state()
    
    def __str__(self):
        return self.puzzle.__str__()