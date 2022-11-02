from random import randint

def create_grids():
    HIDDEN_BOARD = [[" "] * game_size for x in range(game_size)]
    GUESS_BOARD = [[" "] * game_size for i in range(game_size)]

# credit second half of this function in readme
def print_board(board, game_size):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    top_labels = " "
    seperator = " "
    for letter in range(game_size):
        top_labels += letters[letter]
        seperator = "+-"

    print(top_labels)
    print(seperator)
    
    row_number = 1
    for row in board:
        print("%s|%s|" % (" "+str(row_number) if row_number <
              10 else row_number, "|".join(row)))
        row_number += 1

letters_to_numbers ={
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

while game_size == 0 or game_size <= 7 or game_size > 26:
    try:
        game_size = int(input(
            "Welcome to battleship, please enter a grid size from 8 and 26 keeping in mind the larger the grid the more difficult the game!"))
        if game_size <= 7 or game_size > 26:
            print("Invalid input, please enter a grid size from 8 and 26!")
    except ValueError:
        print("Invalid input, please enter a grid size from 8 and 26!")


def create_ships():
    for ship in range(5):
        ship_row, ship_column = randint(0, game_size-1), randint(0, game_size-1)
        pass

def get_ship_location():
    pass

def count_hit_ships():
    pass

create_grids(game_size)






    
