import math,random

class SudokuGenerator:
    def __init__(self, row_length=9, removed_cells= 70):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0 for i in range(self.row_length)] for j in range(9)]
        self.box_length = int(math.sqrt(row_length))
    #initalizes the SudokuGenerator variables

    def get_board(self):
        return self.board
    #gets the board

    def print_board(self):
        for row in self.board:  # row: ["-", "-", "-"]
            for col in row:
                print(col, end=" ")
            print()
    #prints the board

    def valid_in_row(self, row, num):
        z = True
        x = "gfgfg"
        for val in self.board[row]:
            if num == val:
                x = "invaild"
                z = False
                break
            elif num != val:
                x= "vaild"
        if x == "invaild":
            return z
        else:
            return z
    #test the values in the row and sees if it is vaild for that row then returns True or False

    def valid_in_col(self, col, num):
        z = True
        x = "gfgfg"
        for val in range(self.row_length):
            if self.board[val][col] == num:
                x = "invaild"
                z = False
                break
            elif num != val:
                x= "vaild"
        if x == "invaild":
            return z
        else:
            return z
        # test the values in the col and sees if it is vaild for that col then returns True or False

    def valid_in_box(self, row_start, col_start, num):
        z = True
        x = "gfgfg"
        count = True
        while count:
            if row_start == 0 or row_start == 3 or row_start == 6:
                count = False
            else:
                row_start -= 1
        count1 = True
        while count1:
            if col_start == 0 or col_start == 3 or col_start == 6:
                count1 = False
            else:
                col_start -= 1
        for val in range(row_start,row_start+3):
            for val1 in range(col_start,col_start+3):
                if self.board[val][val1] == num:
                    x = "invaild"
                    z = False
                    break
                elif num != val:
                    x= "vaild"
            if x == "invaild":
                break
        return z

    #test if the code is vaild in the specified box and then returns true or false

    def is_valid(self, row, col, num):
        if self.valid_in_box(row,col,num) == True and self.valid_in_col(col,num) == True and self.valid_in_row(row,num) == True:
            return True
        else:
            return False
    #test if the value is vaild in the row, col, box and then returns True or False

    def fill_box(self, row_start, col_start):
        num = random.randint(1, 9)
        for val in range(3):
            for val1 in range(3):
                while self.valid_in_box(row_start,col_start,num) == False:
                    num = random.randint(1,9)
                self.board[row_start+val][col_start+val1] = num

    # fills the box with values that are vaild
    def fill_diagonal(self):
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)
    #fills the diagonal boxes with values from the starting position of (0,0),(3,3) and (6,6)
    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False
        #fills the remaining values of the board that are missing
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)
    #calls upon the fill function and fills the board with the values
    def remove_cells(self):
        count = self.removed_cells
        while count != 0:
            col = random.randint(0, 8)
            row = random.randint(0, 8)
            if self.board[col][row] != 0:
                count -= 1
            self.board[col][row] = 0
    #removes the number of cells that are requested from either hard, med, or easy


def generate_sudoku(size, removed):
        sudoku = SudokuGenerator(size, removed)
        sudoku.fill_values()
        board = sudoku.get_board()
        sudoku.remove_cells()
        board = sudoku.get_board()
        sudoku.print_board()
        return board
    #generates the board
