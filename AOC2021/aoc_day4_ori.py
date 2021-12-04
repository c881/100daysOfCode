BOARD_SIZE = 5

def get_input(path):
    with open(path, 'r') as f:
        return f.readlines()

def get_numbers(inpt):
    return [int(num) for num in inpt[0].strip().split(',')]

def get_boards(boards_inpt):
    i = 0
    boards = []
    while i < len(boards_inpt):
        boards.append(boards_inpt[i: i + BOARD_SIZE])
        i += BOARD_SIZE + 1

    for board in boards:
        for i, line in enumerate(board):
            board[i] = [int(num) for num in line.strip().split()]

    return boards


def mark_number_on_board(board, num):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == num:
                board[i][j] = 'X'
                return True
    return False


def check_rows(board):
    marks = 0
    for row in board:
        for col in row:
            if col == 'X':
                marks += 1
        if marks == BOARD_SIZE:
            return True
        else:
            marks = 0
    return False


def check_cols(board):
    marks = 0
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[j][i] == 'X':
                marks += 1
        if marks == BOARD_SIZE:
            return True
        else:
            marks = 0
    return False


def bingo(boards, numbers, first_win=True):
    winning_board = None
    winning_num = None
    prev_wins = []
    for num in numbers:
        for i, board in enumerate(boards):
            if board not in prev_wins:
                mark_number_on_board(board, num)
                if check_rows(board) or check_cols(board):
                    if first_win:
                        return board, num
                    else:
                        winning_board = board
                        winning_num = num
                        prev_wins.append(board)

    return winning_board, winning_num


def sum_unmarked(board):
    unmarked_sum = 0
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] != 'X':
                unmarked_sum += board[i][j]
    return unmarked_sum


def part1(path, first_win=True):
    inpt = get_input(path)
    numbers = get_numbers(inpt)
    boards = get_boards(inpt[2:])
    winning_board, winning_num = bingo(boards, numbers, first_win)
    return sum_unmarked(winning_board) * winning_num


def part2(path):
    return part1(path, first_win=False)


print(f"Part 1 Result: {part1('inpt4.txt')}")
print(f"Part 2 Result : {part2('inpt4.txt')}")
