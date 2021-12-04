class Board:
    counter = 0
    def __init__(self, board):
        self.board = board
        self.counter = Board.counter
        Board.counter += 1

    def __str__(self):
        text = f"board num: {self.counter}\n"
        for line in self.board:
            text += " ".join(line) +"\n"
        return text

    def num_picked(self, number):
        for i in range(5):
            for j in range(5):
                if self.board[i][j] == number:
                    self.board[i][j] = 'x'
                    return
        return

    def is_winner(self):
        for i in range(5):
            count = 0
            for j in range(5):
                if self.board[i][j] == 'x':
                    count += 1
            if count == 5:
                return True

        for i in range(5):
            count = 0
            for j in range(5):
                if self.board[j][i] == 'x':
                    count += 1
            if count == 5:
                return True


with open("day4_input_a.txt","r") as num_file:
    numbers_chosen = [int(num) for num in num_file.readline().strip().split(',')]

with open("day4_input.txt","r") as boards_file:
    lines = [line.strip().split() for line in boards_file.readlines()]

board = []
boards = []
for line in lines:
    if len(line) != 0:
        board.append(line)
    else:
        boards.append(Board(board))
        board = []

has_winner = -1
last_number = -1
for num in numbers_chosen:
    if last_number < 0:
        for board in boards:
            board.num_picked(num)
        for board in boards:
            if board.is_winner():
                has_winner = board.counter
                if has_winner:
                    last_number = num

print(f"winning board = {has_winner}, last number was {last_number}")