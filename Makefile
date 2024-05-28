NAME=n-puzzle
SRCS= srcs
PYTHON= python3
PATH_PUZZLE= ${SRCS}/puzzle

all: solvable ${NAME}

solvable: ${NAME}
	@${PYTHON} ${SRCS}/npuzzle-gen.py 3 -s > ${PATH_PUZZLE};
	
unsolvable: ${NAME}
	@${PYTHON} ${SRCS}/npuzzle-gen.py 3 -u > ${PATH_PUZZLE};

${NAME}:
	@${PYTHON} ${SRCS}/main.py --path ${PATH_PUZZLE} 

clean:
	@echo clean

fclean: clean

re: fclean all