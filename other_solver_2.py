import random
import timeit
time = timeit.default_timer()


board = [[random.randint(1,9) for j in range(0,9)] for i in range(0,9)]


def validSolution(board):
    boxes = validate_boxes(board)
    cols = validate_cols(board)
    rows = validate_rows(board)
    return boxes and cols and rows


def validate_boxes(board):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            nums = board[i][j:j + 3] + board[i + 1][j:j + 3] + board[i + 2][j:j + 3]
            if not check_one_to_nine(nums):
                return False
    return True


def validate_cols(board):
    transposed = zip(*board)
    for row in transposed:
        if not check_one_to_nine(row):
            return False
    return True


def validate_rows(board):
    for row in board:
        if not check_one_to_nine(row):
            return False
    return True


def check_one_to_nine(lst):
    check = range(1, 10)
    return sorted(lst) == check


now = timeit.default_timer()


print(now - time)

#1.5799999999999842e-05
