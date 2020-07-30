
import random
import timeit
time = timeit.default_timer()


board = [[random.randint(1,9) for j in range(0,9)] for i in range(0,9)]

def valid_solution(board):
    blocks = [[board[x+a][y+b] for a in (0, 1, 2) for b in (0, 1, 2)] for x in (0, 3, 6) for y in (0, 3, 6)]
    return not filter(lambda x: set(x) != set(range(1, 10)), board + zip(*board) + blocks)

now = timeit.default_timer()


print(now - time)


#1.4299999999998342e-05

