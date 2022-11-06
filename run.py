from random import randint


def create_grids(size):
    global HIDDEN_BOARD
    HIDDEN_BOARD = [[" "] * game_size for x in range(size)]
    global GUESS_BOARD
    GUESS_BOARD = [[" "] * game_size for i in range(size)]

# credit second half of this function in readme


def print_board(board, size):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    top_labels = "   "
    seperator = "  "
    for letter in range(size):
        top_labels += letters[letter] + " "
        seperator += "+-"

    print(top_labels)
    print(seperator)

    row_number = 1
    for row in board:
        print("%s|%s|" % (" "+str(row_number) if row_number <
              10 else row_number, "|".join(row)))
        row_number += 1


letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
    'K': 10,
    'L': 11,
    'M': 12,
    'N': 13,
    'O': 14,
    'P': 15,
    'Q': 16,
    'R': 17,
    'S': 18,
    'T': 19,
    'U': 20,
    'V': 21,
    'W': 22,
    'X': 23,
    'Y': 24,
    'Z': 25
}

game_size = 0

while game_size == 0 or game_size <= 3 or game_size > 26:
    try:

        print("Welcome to battleship, please enter a grid size from 8 and 26")
        print("keeping in mind the larger the grid the harder the game!")
        game_size = int(input("Please enter a size: "))
        if game_size <= 3 or game_size > 26:
            print("Invalid input, please enter a grid size from 8 and 26!")
    except ValueError:
        print("Invalid input, please enter a grid size from 8 and 26!")


def create_ships(board, size):
    for _ in range(5):
        ship_row, ship_column = randint(
            0, size-1), randint(0, size-1)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = randint(
                0, size-1), randint(0, size-1)
        board[ship_row][ship_column] = "X"


def get_ship_location(size):
    row = 0
    while row < 1 or row > size:
        try:
            row = int(input("Enter the row of the ship: "))
            if row < 1 or row > size:
                print("Not a relevant choice, please select a valid row")

        except ValueError:
            print("Not a relevant choice, please select a valid row")

    column = input("Enter the column of the ship: ").upper().strip()
    columns = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")[: size]
    while column not in columns or len(column) == 0:
        print("Not a relevant choice, please select a valid column")
        column = input("Enter the column of the ship: ").upper()
    return int(row) - 1, letters_to_numbers[column]


def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


create_grids(game_size)
create_ships(HIDDEN_BOARD, game_size)
print(HIDDEN_BOARD)
turns = 6
while turns > 0:
    print("Guess a battleship location!")
    print_board(GUESS_BOARD, game_size)
    row, column = get_ship_location(game_size)
    GUESS = GUESS_BOARD[row][column]
    if GUESS == '-' or GUESS == 'X':
        print("You already guessed this location")
    elif HIDDEN_BOARD[row][column] == 'X':
        print("Hit")
        GUESS_BOARD[row][column] = 'X'
        turns -= 1
    else:
        print('You Missed')
        GUESS_BOARD[row][column] = '-'
        turns -= 1
    print("You have " + str(turns) + " turns left.")
    if turns == 0:
        print("you ran out of turns, better luck next time.")
        print("You have hit ", count_hit_ships(GUESS_BOARD), "ship[s].")
    if count_hit_ships(GUESS_BOARD) == 5:
        print("Congratulations, you win!")
        break
