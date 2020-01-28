import pylab as PL
import numpy as np

def f(k, x):
    return k * x * (1 - x)

# draw a bifurcation diagram

def plot_bifurcation(x0=0.01, k_start=0, k_end=4.0, dk=0.005, sampling_start_time=1000, sample_no=200):
    result_k = []
    result_x = []

    k = k_start
    while k <= k_end:
        x = x0
        for t in range(sampling_start_time):
            x = f(k, x)
        for t in range(sample_no):
            x = f(k, x)
            result_k.append(k)
            result_x.append(x)
        k += dk

    PL.plot(result_k, result_x, 'k.', markersize=0.1)
    PL.show()

#plot_bifurcation(x0=0.1)

BOARD_SIZE = 100
startK = 0
endK = 3.5
deltaK = 0.01
SAMPLING_START_TIME = 20
SAMPLE_NO = 20


def f(k, x):
    return k * x * (1 - x)

def zeros_board():
    return np.zeros((BOARD_SIZE, BOARD_SIZE))

def random_board():
    return np.array([[np.random.rand() for j in range(BOARD_SIZE)] for i in range(BOARD_SIZE)])

def avg_neighbour(board, x, y):
    neighbourhood = board[max(0,x-1):min(x+2, board.shape[0]), max(0,y-1):min(y+2, board.shape[1])]
    size = neighbourhood.shape[0] * neighbourhood.shape[1]
    return np.sum(neighbourhood) / size

# def get_limit(k, board):
#     for limit_iter in range(limit_range):
#         for i in range(BOARD_SIZE):
#             for j in range(BOARD_SIZE):
#                 board[i, j] = f(k, board[i, j])

def get_next_board(board, k):
    next_board = zeros_board()
    for i in range(len(board)):
        for j in range(len(board)):
            next_board[i, j] = f(k, avg_neighbour(board, i, j))
    return next_board

def run():
    result_k = []
    result_x = []
    k = startK
    try:
        while k <= endK:
            print(k)
            board = random_board()
            for t in range(SAMPLING_START_TIME):
                board = get_next_board(board, k)
            for t in range(SAMPLE_NO):
                next_board = get_next_board(board, k)
                avg_x = np.average(board)
                x_n_plus_1 = f(k, avg_x) - k * np.var(next_board)
                board = next_board
                result_k.append(k)
                result_x.append(x_n_plus_1)
                if k < 3.0: break
            k += deltaK
    except KeyboardInterrupt:
        print('interrupt')
    PL.plot(result_k, result_x, 'b.', markersize=0.2)
    PL.show()

run()
