DEBUG = False

class SudokuPuzzle:
    def __init__(self, values):
        self.board = Board(values)

    def solve(self):
        while True:
            cell = self.board.current_cell()
            if cell == None:
                break

            # Cheap way to see if the constants passed in are valid
            if cell.is_constant:
                cons = cell.value
                cell.value = 0
                if not self.is_valid(cons):
                    return False
                cell.value = cons
            # Check candidates. Walk back and replenish candidates on failure
            else:
                if not self.try_candidates(cell):
                    cell.regen_candidates()
                    cell.value = 0
                    self.board.back()

                    # Skip over constants
                    while self.board.current_cell().is_constant:
                        try:
                            self.board.back()
                        except:
                            # Main exit for an invalid puzzle
                            return False

                    continue

            self.board.advance()
        return True

    # Try all remaining candidates for position
    def try_candidates(self, cell):
        candidates = cell.candidates
        while candidates:
            ca = candidates.pop()
            if DEBUG: print("trying", ca, self.board.row_as_str())

            if self.is_valid(ca):
                cell.value = ca
                return True

            if DEBUG: print("failed at", self.board.row_as_str())
        return False

    # Check row, col, or box
    def is_in(self, board_dim, ca_value):
        for c in board_dim:
            if ca_value == c.value:
                return True

        return False

    # Checks ca at idx for valid row, col, and box
    def is_valid(self, ca_value):
        return (not self.is_in(self.board.current_row(), ca_value)
                and not self.is_in(self.board.current_col(), ca_value)
                and not self.is_in(self.board.current_box(), ca_value))

    def __str__(self):
        return f"{self.board}"

class Board:
    def __init__(self, values):
        self.__cells = [Cell(value) for value in values]
        self.__idx = 0
        self.size = len(self.__cells)

    def current_cell(self):
        if self.__idx < self.size:
            return self.__cells[self.__idx]
        else:
            return None

    def advance(self):
        if self.__idx < self.size:
            self.__idx += 1
        else:
            raise Exception('invalid index in advance()')

    def back(self):
        if self.__idx > 0:
            self.__idx -= 1
        else:
            raise Exception('invalid index in back()')

    def current_row(self):
        row_idx = self.__idx - (self.__idx % 9)
        return self.__cells[row_idx:row_idx+9]

    def current_col(self):
        return self.__cells[self.__idx%9::9]

    def current_box(self):
        # The global row we are in
        row_offset = int((self.__idx - (self.__idx % 9)) / 9)
        # The local row in the box
        box_row_offset = row_offset % 3
        # The leftmost index of the box (in the current row)
        box_row_left_idx = self.__idx - (self.__idx % 3)
        # The top left index of the box
        box_top_left_idx = box_row_left_idx - (box_row_offset * 9)
        box = []
        # Add 3 values for each leftmost index of the box
        for i in [box_top_left_idx, box_top_left_idx+9, box_top_left_idx+18]:
            box.extend(self.__cells[i:i+3])
        return box

    def row_as_str(self):
        row = self.current_row()
        col_idx = self.__idx % 9
        row[col_idx] = "X"
        out = "["
        for x in row:
            out += " %s" % x
        out += " ]"
        return out

    def __str__(self):
        s = ""
        for idx in range(self.size):
            if idx % 9 == 0: s += "\n"
            s += f"{self.__cells[idx]} "
        return s + "\n"

class Cell:
    def __init__(self, value):
        self.value = value
        self.is_constant = True if value != 0 else False
        self.regen_candidates()

    def regen_candidates(self):
        self.candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __str__(self):
        return f"\033[94m[{self.value}]\033[0m" if self.is_constant else f"[{self.value}]"
