DEBUG = False

def print_board(board):
    for idx in range(len(board)):
        if idx % 9 == 0: print()
        print("%s " % board[idx], end="")
    print("\n")

def current_row(board, idx):
    row_idx = idx - (idx % 9)
    return board[row_idx:row_idx+9]

def current_col(board, idx):
    return board[idx%9::9]

def current_box(board, idx):
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
        box.extend(board[i:i+3])
    return box

# Check row, col, or box (passed in by get_dim())
def is_in(board, get_dim, idx, ca):
    if ca in get_dim(board, idx):
        return True
    else:
        return False

def row_as_str(board, idx):
    row = get_row(board, idx)
    col_idx = idx % 9
    row[col_idx] = "X"
    out = "["
    for x in row:
        out += " %s" % x
    out += " ]"
    return out

# Checks ca at idx for valid row, col, and box
def is_valid(board, idx, ca):
    return (not is_in(board, current_row, idx, ca)
            and not is_in(board, current_col, idx, ca)
            and not is_in(board, current_box, idx, ca))

# Try all remaining candidates for position
def try_candidates(board, idx, candidates):
    while candidates[idx]:
        ca = candidates[idx].pop()
        if DEBUG: print("trying", ca, row_as_str(board, idx))

        if is_valid(board, idx, ca):
            board[idx] = ca
            return True
    if DEBUG: print("failed at", row_as_str(board, idx))

    return False

def solve(board):
    # Create a list of candidates for every position in the board
    candidates = [[1, 2, 3, 4, 5, 6, 7, 8, 9] for i in board]

    # List indicating whether the positions are constants
    constants = [v != 0 for v in board]

    idx = 0
    while idx < len(board):
        # Main exit for an invalid puzzle
        if idx < 0: return False

        # Cheap way to see if the constants passed in are valid
        if constants[idx]:
            cons = board[idx]
            board[idx] = 0
            if not is_valid(board, idx, cons):
                return False
            board[idx] = cons
        # Check candidates. Walk back and replenish candidates on failure
        else:
            if not try_candidates(board, idx, candidates):
                candidates[idx] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                board[idx] = 0
                idx -= 1
                # Skip over constants
                while constants[idx]:
                    idx -= 1
                continue

        idx += 1
    return True
