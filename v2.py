from graph import Graph

class SudokuPuzzle:
    def __init__(self, board):
        self.graph = Graph(board, [1, 2, 3, 4, 5, 6, 7, 8, 9])

        # Used for printing
        self.constants = [v != 0 for v in board]

        # Connect all nodes in for each row
        for idx in range(self.graph.size):
            if idx % 9 == 0:
                self.graph.connect_nodes(self.__row_for(idx))

        # Connect all nodes in for each column
        for idx in range(9):
            self.graph.connect_nodes(self.__col_for(idx))

        # Connect all nodes in for each box. Each box here is represented by its top left
        # index
        for idx in range(self.graph.size):
            if idx % 27 == 0:
                for idx in [idx, idx+3, idx+6]:
                    self.graph.connect_nodes(self.__box_for(idx))

    def __row_for(self, idx):
        row_idx = idx - (idx % 9)
        return self.graph.nodes[row_idx:row_idx+9]

    def __col_for(self, idx):
        return self.graph.nodes[idx%9::9]

    def __box_for(self, idx):
        # The global row we are in
        row_offset = int((idx - (idx % 9)) / 9)
        # The local row in the box
        box_row_offset = row_offset % 3
        # The leftmost index of the box (in the current row)
        box_row_left_idx = idx - (idx % 3)
        # The top left index of the box
        box_top_left_idx = box_row_left_idx - (box_row_offset * 9)
        box = []
        # Add 3 values for each leftmost index of the box
        for i in [box_top_left_idx, box_top_left_idx+9, box_top_left_idx+18]:
            box.extend(self.graph.nodes[i:i+3])
        return box

    def solve(self):
        # Make sure the constants are valid first
        if any(node.color != 0 and not node.is_valid() for node in self.graph.nodes):
            return False

        return self.graph.color_nodes()

    def __str__(self):
        s = ""
        for idx in range(self.graph.size):
            if idx % 9 == 0: s += "\n"
            value = self.graph.nodes[idx].color
            s += f"\033[94m[{value}]\033[0m " if self.constants[idx] else f"[{value}] "
        return s + "\n"
