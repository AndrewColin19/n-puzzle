import re

SIZE_REG = r'^[\d]+[\s]*$'
PUZZLE_REG = r'^((\d+)+[\s]*)+$'

def custom_strip(s: str):
    return " ".join(s.split())

def remove_comment(s: str):
    while s.find('#') != -1:
        start = s.index('#')
        end = start
        while s[end] and s[end] != '\n':
            end += 1
        s = s.replace(s[start:end], '')
    return s

def puzzle_parser(file_or_path: str) -> tuple[int, list]:
    puzzle = []
    size = 0
    with open(file_or_path) as file:
        s = file.read()
        i = 0
        s = remove_comment(s)
        rows = s.split('\n')
        error = False
        for i in range(len(rows)):
            rows[i] = rows[i].strip()
            if rows[i] == '':
                continue
            if re.match(SIZE_REG, rows[i]):
                if size != 0:
                    error = True
                size = int(rows[i])
            elif re.match(PUZZLE_REG, rows[i]):
                for v in custom_strip(rows[i]).split(' '):
                   puzzle.append(int(v))
            else:
                error = True
            if error:    
                raise Exception(f"Incorrect line: '{rows[i]}'")
    if size < 3 and not puzzle:
        raise Exception("empty file")
    return size, puzzle