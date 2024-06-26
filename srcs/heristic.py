def hamming(size: int, candidate: tuple[int], solved: tuple[int]):
    h = 0
    for i in range(size * size):
        if candidate[i] != 0 and candidate[i] != solved[i]:
            h += 1
    return h

def manhattan_distance(size, puzzle, goal):
    distance = 0
    for index, value in enumerate(puzzle):
        if value != 0:
            goal_index = goal.index(value)
            current_row, current_col = divmod(index, size)
            goal_row, goal_col = divmod(goal_index, size)
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    
    return distance

def linear_conflicts(size: int, puzzle: tuple[int], goal: tuple[int]):
    conflicts = 0
    
    def count_conflicts(line: tuple[int], goal_line: tuple[int]):
        conflict_count = 0
        for i in range(len(line)):
            if line[i] != 0 and goal_line[i] != 0 and goal_line[i] > line[i]:
                conflict_count += 1
        return conflict_count

    for row in range(size):
        row_start = row * size
        row_end = row_start + size
        current_row = puzzle[row_start:row_end]
        goal_row = goal[row_start:row_end]
        conflicts += count_conflicts(current_row, goal_row)

    for col in range(size):
        current_column = [puzzle[row * size + col] for row in range(size)]
        goal_column = [goal[row * size + col] for row in range(size)]
        conflicts += count_conflicts(current_column, goal_column)
    
    return conflicts

def heuristic_linear_conflicts(size: int, puzzle: tuple[int], goal: tuple[int]):
    return manhattan_distance(size, puzzle, goal) + 2 * linear_conflicts(size, puzzle, goal)


heristics = {
    1: manhattan_distance,
    2: hamming,
    3: linear_conflicts,
    4: heuristic_linear_conflicts
}