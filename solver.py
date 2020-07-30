
import random
import timeit
time = timeit.default_timer()

board = [[random.randint(1,9) for j in range(0,9)] for i in range(0,9)]

def valid_solution(board):
    for a in range(0,9):
        for b in range(0,9):
            #Checks the 3x3 grid
            if a % 3 == 0 and b % 3 == 0:
                        for d in range(1,3):
                            for e in range(1,3):
                                if board[a][b] == board[a+e][b+d] or board[a][b] == board[a+d][b+e] or (board[a+d][b+e] == board[a+e][b+d] and d!=e):
                                    print(a,b)
                                    return False
                                else:
                                    continue
            #checks the rows and columns
            for c in range(0,9):
                if c !=b and c != a:
                    if board[a][b] != board[a][c] and board[a][b] != board[c][b]:
                        continue
                    else:
                        return False
    return True

now = timeit.default_timer()


print(now - time)

#Given a controlled board, i ran tests to see the fastest algorithm

#1.5000000000001124e-05
