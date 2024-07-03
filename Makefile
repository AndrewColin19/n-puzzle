NAME = n-puzzle
SRCS = srcs
PYTHON = python3
PATH_PUZZLE = ${SRCS}/puzzles/

all: solvable ${NAME}

${NAME}:
	@${PYTHON} ${SRCS}/main.py -p ${PATH_PUZZLE}/3x3

clean:
	@echo clean

fclean: clean

re: fclean all