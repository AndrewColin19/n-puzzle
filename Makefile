

all:


puzzle:
    @echo python3 srcs/gen_puzzle.py $(filter-out $@,$(MAKECMDGOALS))
%:
    @: