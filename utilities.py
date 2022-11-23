import random


def print_board(game_board: [[int, ], ]) -> None:
    """
    Print a formatted version of the game board.
    :param game_board: a 4x4 2D list of integers representing a game of 2048
    """
    for row in game_board:
        print("+----+" * 4)
        print(''.join(f"|{cell if cell else '':^4}|" for cell in row))
        print("+----+" * 4)


def generate_piece(game_board: [[int, ], ], user_input=False) -> {str: int, }:
    """
    Generates a value and coordinates for the next number to be placed on the board.
    Will raise error if the provided board is full.
    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :param user_input: specifies type of piece generation: random or user-specified
    :return: dictionary with the following keys: {'row': int, 'column': int, 'value': int}
    """
    empty_cells = [(y, x) for y, row in enumerate(game_board) for x, cell in enumerate(row) if not cell]
    if not empty_cells:
        raise Exception("Board Full")
    if user_input:
        return dict(zip(('column', 'row',  'value'), (int(i) for i in input("column,row,value:").split(','))))
    return dict(
        zip(('row', 'column', 'value'), (*random.choice(empty_cells), (2 if random.random() * 100 < 90 else 4))))

