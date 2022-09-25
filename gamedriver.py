from gameboard import GameBoard


class GameDriver:

    def __init__(self):
        self.rows = int(input('Please input total number of rows: '))
        self.cols = int(input('Please input total number of cols: '))
        self.mines = int(input('Please input total number of mines: '))
        self.board = GameBoard(self.rows, self.cols, self.mines)

    def finished(self):
        return self.board.finished()

    def next(self):
        row = int(input('Please input a row number: '))
        col = int(input('Please input a col number: '))
        self.board.dig(row, col)
        self.board.print_board()
