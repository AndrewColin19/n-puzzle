import time
from puzzle import Puzzle
from node import Node
from queue import PriorityQueue

class Solver():
    def __init__(self, puzzle: Puzzle) -> None:
        self.first_step = puzzle

    def a_star_solve(self, heuristic, cost):
        queue = PriorityQueue()
        n = Node(self.first_step, heuristic=heuristic, cost=cost)
        queue.put(n)
        closed = set()
        start = time.time()
        while not queue.empty():
            current = queue.get()
            if current.solved:
                break
            closed.add(current.state)
            for move in current.actions:
                node = Node(move(), current, heuristic, cost)
                if node.state in closed:
                    continue 
                queue.put(node)
        end = time.time() - start
        return current.get_path(), queue.qsize(), len(closed), end #path, complexity in size, complexity in time, time

    def solve(self, heuristic = 1, cost = 1):
        return self.a_star_solve(heuristic, cost)
    
    def __str__(self) -> str:
        return self.first_step.__str__()
