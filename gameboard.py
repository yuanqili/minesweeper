import random

from tile import Tile


class MineGenerator:

    def __init__(self, num_mines, total):
        self.num_mines = num_mines
        self.mines = [True] * num_mines + [False] * (total - num_mines)
        random.shuffle(self.mines)
        self.index = 0

    def next(self):
        has_mine = self.mines[self.index]
        self.index += 1
        return has_mine


class GameBoard:

    def __init__(self, rows, cols, num_mines):
        self._rows = rows
        self._cols = cols
        self._finished = False
        self._board = []
        generator = MineGenerator(num_mines, rows * cols)
        for _ in range(rows):
            row = [Tile(generator.next()) for _ in range(cols)]
            self._board.append(row)

    def finished(self):
        return self._finished

    def dig(self, row, col):
        self._finished = self._board[row][col].has_mine
        if self._finished:
            self._board[row][col].dig()
            return

        # Breadth first search (BFS)
        auto_dig = [(row, col)]
        while len(auto_dig) > 0:
            tile_coord = auto_dig.pop(0)
            row, col = tile_coord[0], tile_coord[1]
            print(f'digging {row, col}')
            self._board[row][col].dig()
            if self._count_mines(row, col) != 0:
                continue
            for row_offset, col_offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                n_row, n_col = row + row_offset, col + col_offset
                if not self._is_valid_coord(n_row, n_col):
                    continue
                if self._board[n_row][n_col].has_dug:
                    continue
                if self._count_mines(n_row, n_col) != 0:
                    continue
                print(f'\tfound {(n_row, n_col)}')
                auto_dig.append((n_row, n_col))

    def print_board(self):
        for row in range(self._rows):
            for col in range(self._cols):
                self._print_tile(row, col)
            print()

    def _print_tile(self, row, col):
        tile = self._board[row][col]
        if not tile.has_dug:
            print('o', end='')
            return
        if tile.has_mine:
            print('x', end='')
            return
        num_mines = self._count_mines(row, col)
        if num_mines == 0:
            print(' ', end='')
        else:
            print(num_mines, end='')

    def _is_valid_coord(self, row, col):
        if row < 0 or row >= self._rows:
            return False
        if col < 0 or col >= self._cols:
            return False
        return True

    def _count_mines(self, row, col):
        neighbors = []
        offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for offset in offsets:
            n_row, n_col = row + offset[0], col + offset[1]
            if not self._is_valid_coord(n_row, n_col):
                continue
            neighbors.append(self._board[n_row][n_col])
        return sum([n.has_mine for n in neighbors])
