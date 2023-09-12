import copy


def initial_state():
    return ((7, 2, 4, 5, 0, 6, 8, 3, 1), 1, 1)


def is_goal(s):
    return s[0] == (1, 2, 3, 4, 5, 6, 7, 8, 0)


def successors(s):
    _, r, c = s #state , row, column
    new_r, new_c = r-1, c
    if is_valid(new_r, new_c): #left
        yield move_blank(s, new_r, new_c), 1
    new_r, new_c = r+1, c
    if is_valid(new_r, new_c): #right
        yield move_blank(s, new_r, new_c), 1
    new_r, new_c = r, c-1
    if is_valid(new_r, new_c): #up
        yield move_blank(s, new_r, new_c), 1
    new_r, new_c = r, c+1
    if is_valid(new_r, new_c): #down
        yield move_blank(s, new_r, new_c), 1


def is_valid(r, c):
    return 0 <= r <= 2 and 0 <= c <= 2


def move_blank(s, new_r, new_c): #1,1->0,1
    board, r, c = s
    new_board = list(board)
    new_board[r*3 + c] = new_board[new_r*3 + new_c] # update 0 to data
    new_board[new_r*3 + new_c] = 0                  # update data to 0
    return (tuple(new_board), new_r, new_c)         # update state

def h1(s):
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    board, _, _ = s
    res = 0
    # The for loop counts the number of elements that is different from
    # the goal configuration.
    # We start from index 1 to 8 because the blank is excluded.
    for idx in range(1, 9):
        if goal[idx] != board[idx]:
            res += 1
    return res

def h3(s):
    # implement this function
    board, _, _ = s
    i_1,i_2,i_3,i_4,i_5,i_6,i_7,i_8,i_0, = board

    #defined current position
    c_state = {i_1:(0,0),i_2:(1,0),i_3:(2,0),i_4:(0,1),i_5:(1,1),i_6:(2,1),i_7:(0,2),i_8:(1,2),i_0:(2,2)}
    #defined goal postion
    g_state = {1:(0,0),2:(1,0),3:(2,0),4:(0,1),5:(1,1),6:(2,1),7:(0,2),8:(1,2),0:(2,2)}

    h_value = 0
    
    for i in board:

        c_r,c_c = c_state[i]
        g_r,g_c = g_state[i]

        if (c_r != g_r):
            h_value += 1
        if (c_c != g_c):
            h_value += 1

    return h_value
