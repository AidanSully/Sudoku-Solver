import sys

board = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]

def read_file(file):
    file = file.splitlines()
    for i in range(len(file)):
        for j in range(len(file[i])):
            if file[i][j] == '.':
                board[i][j] == 0
            elif file[i][j].isdigit() and int(file[i][j]) < 10:
                board[i][j] = int(file[i][j])
            else:
                print("Error")
                return False
    return board
    