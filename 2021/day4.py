bingo = open('day4_input.txt', 'r').readlines()
bingo = [line.strip() for line in bingo]

print("Solution 1")

def data_setup(bingo):
    bingo_numbers = [int(x) for x in bingo[0].split(",")]

    bingo_boards = []
    current_board = []

    for line in bingo[1:]:
        if line:
            splitted = line.replace("  ", " ").split(" ")
            current_board.append([int(x) for x in splitted])
        else:
            if current_board:
                bingo_boards.append(current_board)
            current_board = []
    return bingo_numbers, bingo_boards



def mark_board_when_match(board, number):
    for y in range(0,5):
        for x in range(0,5):
            current = board[x][y]
            if (current == number):
                board[x][y] = str(number) + "X"

def check_for_winners(boards):
    winners = []
    for board in boards:
        for t in range(0,5):
            current = board[t][t]
            if ("X" in str(current)):
                result, line = is_line_fully_marked(board, t)
                if result:
                    winners.append(board)
                    break
    return winners

def is_line_fully_marked(board, center):
    horizontal = [board[0][center], board[1][center], board[2][center], board[3][center], board[4][center]]
    vertical   = [board[center][0], board[center][1], board[center][2], board[center][3], board[center][4]]
    if all("X" in str(s) for s in horizontal):
        return True, horizontal
    elif all("X" in str(s) for s in vertical): 
        return True, vertical
    return False, _

def calculate_score(board):
    summ = 0
    for y in range(0,5):
        for x in range(0,5):
            current = board[x][y]
            if ("X" not in str(current)):
                summ += current 
    return summ

bingo_numbers, bingo_boards = data_setup(bingo)

for num in bingo_numbers:
    last_num = num
    for board in bingo_boards:
        mark_board_when_match(board, num)
    
    winner_boards = check_for_winners(bingo_boards)
    if winner_boards:
        break

score = calculate_score(winner_boards[0])
print("Score:", score * last_num)


print("Solution 2")

bingo_numbers, bingo_boards = data_setup(bingo)

for num in bingo_numbers:
    last_num = num
    for board in bingo_boards:
        mark_board_when_match(board, num)
    
    winner_boards = check_for_winners(bingo_boards)
    if winner_boards:

        if (len(bingo_boards) == 1):
            break

        for winner_board in winner_boards:
            bingo_boards.remove(winner_board)

score = calculate_score(bingo_boards[0])
print("Last Winner Score:", score * last_num)