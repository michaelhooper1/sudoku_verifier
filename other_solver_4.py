from itertools import product
import random
import timeit
time = timeit.default_timer()


board = [[random.randint(1,9) for j in range(0,9)] for i in range(0,9)]

def validSolution(board):
    rows = board
    columns = map(list, zip(*board))
    blocks = [[board[i][j] for (i, j) in product(xrange(x, x + 3), xrange(y, y + 3))] for (x, y) in
              product((0, 3, 6), repeat=2)]

    return all(sorted(line) == range(1, 10) for lines in (rows, columns, blocks) for line in lines)


now = timeit.default_timer()


print(now - time)

#1.4699999999999436e-05
