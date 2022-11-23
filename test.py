from main import move
game_board = [[4, 2, 2, 4],
              [8, 4, 4, 2],
              [4, 128, 16, 8],
              [2, 8, 2048, 0]]

user_input = 'a'
test_board1 = str(game_board)

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

move(game_board, user_input)

print(test_board)
print(game_board)