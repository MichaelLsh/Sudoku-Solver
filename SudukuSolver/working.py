board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def solve(bo):
    print(bo)
    find = find_empty(bo)
    if not find:  # recursion's base case
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):  # recursion occurs
                return True

            bo[row][col] = 0  # back-track
    return False

def valid(bo, num, pos):
    """
    :param bo:
    :param num: the number which the player just added in
    :param pos: ()
    :return:
    """
    # check duplicate num among rows
    for i in range(len(bo[0])):
        # check thru each col(each element in row)
        if bo[pos[0]][i] == num and pos != i:  # ignore the pos the player just added the num in (pos == i)
            return False

    # check duplicate num among cols
    for j in range(len(bo)):
        # loop thru each row
        if bo[j][pos[1]] == num and pos[0] != j:
            return False

    # check duplicate num in each 3x3 matrix / box
    # // calculation -> val of 0/1/2
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True


def print_board(bo):
    # len(board) -> # of rows
    for i in range(len(bo)):
        # print row divider of - after every 3 rows
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        # len(board[0]) -> # of columns
        for j in range(len(bo[0])):
            # print the col divider after each 3 cols
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:  # @ the last position of each
                print(bo[i][j])  # print the current square and move to the next row
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:  # if find an empty square
                return (i, j)  # (row_index, col_index)

    return None

