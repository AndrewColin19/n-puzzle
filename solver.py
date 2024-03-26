from puzzle import Puzzle
from node import Node

class Solver():
    def __init__(self, puzzle: Puzzle) -> None:
        self.first_step = puzzle

    def a_star_solve(self, heuristic, cost):
        queue = [Node(self.first_step, heuristic=heuristic, cost=cost)]
        closed = {}
        opened = {}
        while queue:
            current = queue.pop()
            if current.is_solved():
                break
            if current.state in closed:
                 continue
            if current.parent:
                closed[current.parent.state] = current
            for move, action in current.get_actions():
                node = Node(move(), current, action, heuristic, cost=cost)
                if node.state in closed:
                    continue
                if node.state in opened:
                    n = opened[node.state]
                    if n.g <= node.g:
                        continue
                queue.insert(0, node)
                opened[node.state] = node
        return current.get_path(), opened, closed

    def solve(self, heuristic = 1, cost = 1):
        return self.a_star_solve(heuristic, cost)
    
    def __str__(self) -> str:
        return self.first_step.__str__()
