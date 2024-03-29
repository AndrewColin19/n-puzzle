import sys
import random
import os

ERROR = "Error: {} Usage: size=?? -s for solvable or -u for unsolvable path=?? to save file"

def gen_puzzle(size: int, solvable: bool = True) -> list[list]:
    if solvable:
        print(f"Generate solvable puzzle size: {size}")
    else:
        print(f"Generate unsolvable puzzle size: {size}")
    l = [i for i in range(1, size * size)]
    l.append(0)
    if not solvable:
        if l[0] == 0 or l[1] == 0:
            l[-1], l[-2] = l[-2], l[-1]
        else:
            l[0], l[1] = l[1], l[0]
    v = 0
    puzzle = []
    for _ in range(size):
        row = []
        for _ in range(size):
            row.append(l[v])
            v += 1
        puzzle.append(row)
    return puzzle

def push_in_file(path: str, puzzle: list[list]):
    try:
        with open(path, 'w') as file:
            for row in puzzle:
                file.write(",".join([str(v) for v in row]) + "\n")
        print(f"saved in {os.path.abspath(path)}")
    except FileNotFoundError:
        raise Exception(f"No such file or directory: {path}")
    except Exception:
        raise Exception("Unkwnow")

def main(argv: list[str]):
    args = {
        'size': {'type': int, 'min': 3, 'default': 3, 'value': None ,'here': False},
        '-s': {'here': False},
        '-u': {'here': False},
        'path': {'type': str, 'default': 'puzzle', 'value': None, 'here': False}
    }
    for arg in argv:
        find = False
        for key, item in args.items():
            if arg.startswith(key):
                find = True
                item['here'] = True
                if 'value' in item:
                    v = arg.split('=')
                    if len(v) != 2:
                        raise Exception(ERROR.format(f"Invalid {key}"))
                    else:
                        item['value'] = item['type'](v[1])
        if not find:
            raise Exception(ERROR.format(f"Invalid arg {arg}"))
    for item in args.values():
        if not item['here'] and 'default' in item:
            item['value'] = item['default']
    if args['-s']['here'] and args['-u']['here']:
        raise Exception(ERROR.format("Invalid args"))
    if args['size']['value'] < args['size']['min']:
        raise Exception(ERROR.format("Size cannot be lower than 3"))
    puzzle = gen_puzzle(args['size']['value'], False if args['-u']['here'] else True)
    push_in_file(args['path']['value'], puzzle)

if __name__=='__main__':
    try:
        main(sys.argv[1:])
    except Exception as e:
        print(type(e))
        print(ERROR.format(e))
    