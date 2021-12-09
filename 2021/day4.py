import numpy as np


def part1(numbers, boards):
    called_numbers = []
    for n in numbers:
        called_numbers.append(n)
        for b in boards:
            col_condition = np.isin(b, called_numbers).astype(int).sum(axis=1).max()
            row_condition = np.isin(b, called_numbers).astype(int).sum(axis=0).max()
            if row_condition >= 5 or col_condition >= 5:
                return b[~np.isin(b, called_numbers)].sum() * n

def part2(numbers, boards):
    from rich.progress import track
    called_numbers = []
    winning_boards = []
    winning_scores = []
    for n in track(numbers):
        called_numbers.append(n)
        for i, b in enumerate(boards):
            if i in winning_boards:
                continue
            col_condition = np.isin(b, called_numbers).astype(int).sum(axis=1).max()
            row_condition = np.isin(b, called_numbers).astype(int).sum(axis=0).max()
            if row_condition >= 5 or col_condition >= 5:
                winning_boards.append(i)
                winning_scores.append(b[~np.isin(b, called_numbers)].sum() * n)
    return winning_scores[-1]

def parsefile(infile):
    first_line = True
    numbers = None
    boards = []
    curr_board = np.zeros((5,5)).astype(int)
    curr_row = 0
    for line in open(infile):
        if first_line:
            first_line = False
            numbers = [int(i) for i in line.strip().split(',')]
            continue
        if not line.strip():
            if curr_row >= 4:
                boards.append(curr_board)
                curr_board = np.zeros((5,5)).astype(int)
                curr_row = 0
            continue
        curr_board[curr_row, :] = [int(i) for i in line.strip().split()]
        curr_row += 1
    boards.append(curr_board)
    return numbers, boards

def run():
    numbers, boards = parsefile('day4.input')
    print(f'Part 1: {part1(numbers, boards)}')
    print(f'Part 2: {part2(numbers, boards)}')

if __name__ == '__main__':
    run()