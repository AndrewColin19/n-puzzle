from puzzle import Puzzle
from typing import Self

class Node():
    def __init__(self, puzzle: Puzzle, parent = None, cost = 1) -> None:
        self.puzzle = puzzle
        self.size = self.puzzle.size
        self.parent: Node = parent
        self.g = self.parent.g + cost if self.parent is not None else 0
        self.f = self.g + self.puzzle.heristic()
        self.actions = self.puzzle.get_actions()
        self.solved = self.puzzle.solved

    def get_path(self) -> list[Self]:
        node, p = self, []
        while node:
            p.append(node)
            node = node.parent
        p.reverse()
        return p

    @property
    def state(self) -> int:
        return hash(str(self.puzzle.board))
    
    def __str__(self) -> str:
        return str(self.puzzle.board)
    
    def __gt__(self, other: Self):
        return self.f > other.f