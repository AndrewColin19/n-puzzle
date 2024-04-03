NAME=n-puzzle
SRCS= srcs
PYTHON= python3
PATH_PUZZLE= ${SRCS}/puzzle

all: gen ${NAME}

gen:
	@${PYTHON} ${SRCS}/npuzzle-gen.py 3 -s > ${PATH_PUZZLE};

${NAME}:
	@${PYTHON} ${SRCS}/main.py --path ${PATH_PUZZLE} 

clean:
	@echo clean

fclean: clean

re: fclean all