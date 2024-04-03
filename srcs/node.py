from puzzle import Puzzle

class Node():
    def __init__(self, puzzle: Puzzle, parent = None, heuristic = 1, cost = 1) -> None:
        self.puzzle = puzzle
        self.parent: Node = parent
        self.g = self.parent.g + cost if self.parent is not None else 0
        self.f = self.g + self.puzzle.heristic(heuristic)
        self.actions = self.puzzle.get_actions()
        self.solved = self.puzzle.solved
        self.state = self.puzzle.state

    def get_path(self):
        node, p = self, []
        while node:
            p.append(node)
            node = node.parent
        p.reverse()
        return p
    
    def pretty_str(self):
        return self.puzzle.pretty_str()
    
    def __gt__(self, other):
        return self.f > other.f
    
    def __str__(self):
        return self.puzzle.__str__()