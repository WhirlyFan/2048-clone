from utilities import generate_piece, print_board

DEV_MODE = False


def main(game_board: [[int, ], ]) -> [[int, ], ]:
    """
    2048 main function, runs a game of 2048 in the console.

    Uses the following keys:
    w - shift up
    a - shift left
    s - shift down
    d - shift right
    q - ends the game and returns control of the console
    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: returns the ending game board
    """
    # Initialize board's first cell
    # TODO: generate a random piece and location using the generate_piece function
    piece = generate_piece(game_board, DEV_MODE)
    # TODO: place the piece at the specified location
    game_board[piece['row']][piece['column']] = piece['value']
    # Initialize game state trackers
    print_board(game_board)
    # Game Loop
    while True:
        valid_moves = ['w', 'a', 's', 'd', 'q']
        user_input = input("Pick one from ['w', 'a', 's', 'd', 'q']: \n")
        while user_input not in valid_moves:
            user_input = input("Pick one from ['w', 'a', 's', 'd', 'q']: \n")
        if user_input == 'q':
            break
        test_board1 = str(game_board)
        move(game_board, user_input)
        test_board2 = str(game_board)


        # TODO: Reset user input variable

        # TODO: Take computer's turn

        # place a random piece on the board
        if test_board1 != test_board2:
            piece = generate_piece(game_board, DEV_MODE)
            game_board[piece['row']][piece['column']] = piece['value']

        # check to see if the game is over using the game_over function
        if game_over(game_board):
            print('Game Over')
            break
        else:
            print_board(game_board)
        # TODO: Show updated board using the print_board function
        
        # TODO: Take user's turn
        # Take input until the user's move is a valid key
        # if the user quits the game, print Goodbye and stop the Game Loop
        # Execute the user's move

        # Check if the user wins
    return game_board


def move(game_board, user_input):
    if user_input == 'a':
        #shift to the left
        for row in game_board:
            counter = 0
            while 0 in row:
                row.remove(0)
                counter += 1
            for i in range(counter):
                row.append(0)
            #combine logic
            for i in range(len(row) - 1):
                if row[i] == row[i + 1]:
                    row[i + 1] += row[i + 1]
                    row.remove(row[i])
                    row.append(0)

    if user_input == 'd':
        #shift to the right
        for j, row in enumerate(game_board):
            row = row[::-1]
            counter = 0
            while 0 in row:
                row.remove(0)
                counter += 1
            for i in range(counter):
                row.append(0)
            #combine logic
            for i in range(len(row) - 1):
                if row[i] == row[i + 1]:
                    row[i + 1] += row[i + 1]
                    row.remove(row[i])
                    row.append(0)
            game_board[j] = row[::-1]
    
    if user_input == 'w':
        #rotate counter clockwise
        rotated_board = [[], [], [], []]
        for row in game_board:
            for i in range(len(row)):
                rotated_board[i].append(row[i])
        rotated_board = rotated_board[::-1]
        #shift to the left
        for row in rotated_board:
            counter = 0
            while 0 in row:
                row.remove(0)
                counter += 1
            for i in range(counter):
                row.append(0)
            #combine logic
            for i in range(len(row) - 1):
                if row[i] == row[i + 1]:
                    row[i + 1] += row[i + 1]
                    row.remove(row[i])
                    row.append(0)
        #rotate clockwise? honestly idek anymore ive been working all day on this
        rotated_board2 = [[], [], [], []]
        for row in rotated_board:
            for i in range(len(row)):
                rotated_board2[i].append(row[i])
                new_board = [row[::-1] for row in rotated_board2]
        for j in range(4):
            for k in range(4):
                game_board[j][k] = new_board[j][k]

    if user_input == 's':
        #rotate counter clockwise?
        rotated_board = [[], [], [], []]
        for row in game_board:
            for i in range(len(row)):
                rotated_board[i].append(row[i])
        rotated_board = rotated_board[::-1]
        #shift to the right
        for j, row in enumerate(rotated_board):
            row = row[::-1]
            counter = 0
            while 0 in row:
                row.remove(0)
                counter += 1
            for i in range(counter):
                row.append(0)
            #combine logic
            for i in range(len(row) - 1):
                if row[i] == row[i + 1]:
                    row[i + 1] += row[i + 1]
                    row.remove(row[i])
                    row.append(0)       
            game_board[j] = row[::-1]
        #rotate clockwise? honestly idek anymore ive been working all day on this
        rotated_board2 = [[], [], [], []]
        for row in game_board:
            for i in range(len(row)):
                rotated_board2[i].append(row[i])
                new_board = [row[::-1] for row in rotated_board2]
        for j in range(4):
            for k in range(4):
                game_board[j][k] = new_board[j][k]
    return game_board



def game_over(game_board: [[int, ], ]) -> bool:
    """
    Query the provided board's game state.

    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: Boolean indicating if the game is over (True) or not (False)
    """
    status = False
    # TODO: Loop over the board and determine if the game is overd
    for row in game_board:
        if 2048 in row:
            print('You Won!')
            return True
    valid_moves = ['w', 'a', 's', 'd', 'q']
    status = False
    counter = 0
    test_board = [[], [], [], []]
    #returns True if there aren't any 0s in board
    for row in game_board:
        for column in row:
            if column == 0:
                counter += 1
        #adds 1 to counter if there are any pairs in the board
        if any((row[i] == row[i + 1] and row[i] != 0) for i in range(len(row) - 1)):
            counter += 1
    #returns True if there aren't any pairs in the rotated board
    for row in game_board:
        for i in range(len(row)):
            test_board[i].append(row[i])
    test_board = test_board[::-1]
    #adds 1 to counter if there are any pairs in the rotated test board
    for row in test_board:
        if any((row[i] == row[i + 1] and row[i] != 0) for i in range(len(row) - 1)):
            counter += 1    

    if counter == 0:
        status = True
    return status  # TODO: Don't always return false


if __name__ == "__main__":
    main([[0, 0, 0, 0],
          [0, 0, 0, 2],
          [0, 0, 0, 0],
          [0, 0, 0, 0]])
