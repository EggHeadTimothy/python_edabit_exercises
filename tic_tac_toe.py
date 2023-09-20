"""
Tic Tac Toe by Timothy Eden
Date Last Modified: September 20, 2023

This is my implementation of the following challenge from Edabit:
https://edabit.com/challenge/A8gEGRXqMwRWQJvBf
"""


def check_rows(board):
    """
    Each time a row is iterated over, the two flags all_x and all_o are reset to True. If any of the marks in that row
    are O or empty, all_x is set to False, and if any of the marks are X or empty, all_o becomes False (this way, it is
    impossible for both of them to still be set to True at the end). After this, if one of the flags is still set as
    True, a winner has been determined, and the function either returns 'X' or 'O' respectively. If a winner was not
    determined, the function returns an empty string to signal that a winner was not found.
    """
    for row in board:
        all_x = True
        all_o = True
        for mark in row:
            if mark in ['O', 'E']:
                all_x = False
            if mark in ['X', 'E']:
                all_o = False
        if all_x:
            return 'X'
        if all_o:
            return 'O'
    return ''


def tic_tac_toe(board):
    """
    This function uses the helper function check_rows to first check for a winner across a row, then flips the board
    sideways so that columns become rows, and checks for a winner down one of the columns, then finally evaluates for
    a diagonal winner by making 2 rows of the spaces involved in a diagonal win. If check_rows never returns a winner
    under any of these conditions, the function reaches the end and returns 'Draw'.
    """
    # check if anyone won horizontally
    winner = check_rows(board)
    if winner != '':
        return winner

    # create the columns as lists, and check if anyone won vertically
    column1 = [board[0][0], board[1][0], board[2][0]]
    column2 = [board[0][1], board[1][1], board[2][1]]
    column3 = [board[0][2], board[1][2], board[2][2]]
    sideways_board = [column1, column2, column3]

    winner = check_rows(sideways_board)
    if winner != '':
        return winner

    # create the diagonals as lists, and check if anyone won diagonally
    diagonal1 = [board[0][0], board[1][1], board[2][2]]
    diagonal2 = [board[2][0], board[1][1], board[0][2]]
    diagonal_board = [diagonal1, diagonal2]

    winner = check_rows(diagonal_board)
    if winner != '':
        return winner

    return 'Draw'


def main():
    assert tic_tac_toe([
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["O", "X", "X"]
    ]) == "X"

    assert tic_tac_toe([
        ["O", "O", "O"],
        ["O", "X", "X"],
        ["E", "X", "X"]
    ]) == "O"

    assert tic_tac_toe([
        ["X", "X", "O"],
        ["O", "O", "X"],
        ["X", "X", "O"]
    ]) == "Draw"

    assert tic_tac_toe([
        ["X", "O", "O"],
        ["X", "O", "O"],
        ["X", "X", "X"]
    ]) == "X"

    assert tic_tac_toe([
        ["X", "X", "O"],
        ["O", "O", "X"],
        ["X", "X", "O"]
    ]) == "Draw"

    assert tic_tac_toe([
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["E", "E", "X"]
    ]) == "X"

    assert tic_tac_toe([
        ["X", "O", "E"],
        ["X", "O", "E"],
        ["E", "O", "X"]
    ]) == "O"


if __name__ == '__main__':
    main()
