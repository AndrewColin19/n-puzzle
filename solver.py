from puzzle import Puzzle
from node import Node

class Solver():
    def __init__(self, puzzle: Puzzle) -> None:
        self.first_step = puzzle

    def a_star_solve(self):
        queue = [Node(self.first_step)]
        g = 0
        while queue:
            g += 1
            node = queue.pop()
            if node.is_solved():
                break
            smart_n = None
            for move, action in node.get_actions():
                n = Node(move(), node, action, g)
                if smart_n is None:
                    smart_n = n
                elif smart_n.f > n.f:
                    smart_n = n
            queue.insert(0, smart_n)
        return node.get_path()

    def solve(self, algo = None, heuristic = None):
        return self.a_star_solve()
    
    def __str__(self) -> str:
        return self.first_step.__str__()
