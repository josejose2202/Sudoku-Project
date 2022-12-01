import math,random

class SudokuGenerator:
    def __init__(self, row_length=9, removed_cells= 30):
        self.row_length = row_length
        self.remove_cells = removed_cells
        self.box_length = math.sqrt(row_length)
    def get_board(self):
        return [["-" for i in range(self.row_length)] for j in range(9)]

    def print_board(self):
        for row in self.get_board():  # row: ["-", "-", "-"]
            for col in row:
                print(col, end=" ")
            print()
