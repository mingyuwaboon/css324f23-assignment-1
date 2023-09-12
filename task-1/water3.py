def initial_state():
    '''(a,b,c) = bottles max(8,5,3)'''
    return (8, 0, 0)

def is_goal(s):
    '''a == 4 and b == 4'''
    if(s[0] == 4 and s[1] == 4):
        return True

def successors(s):
    ''' return list of next state and cost'''
    a, b, c = s
    # try a  
    if(a > 0):
        if(b < 5):
            left_b = 5-b
            if(left_b <= a):
                yield((a-left_b, b+left_b, c),left_b)
            if(left_b > a):
                yield((0, b+a, c),a)
        if(c < 3):
            left_c = 3-c
            if(left_c <= a):
                yield((a-left_c, b, c+left_c),left_c)
            if(left_c > a):
                yield((0, b, c+a),a)
    if(b > 0):
        if(a < 8):
            left_a = 8-a
            if(left_a <= b):
                yield((a+left_a, b-left_a, c),left_a)
            if(left_a > b):
                yield((a+b,0,c),b)
        if(c < 3):
            left_c = 3-c
            if(left_c <= b):
                yield((a, b-left_c, c+left_c),left_c)
            if(left_c > b):
                yield((a, 0, c+b),b)
    if(c > 0):
        if(a < 8):
            left_a = 8-a
            if(left_a <= c):
                yield((a+left_a,b,c-left_a),left_a)
            if(left_a > c):
                yield((a+c, b, 0),c)
        if(b < 5):
            left_b = 5-b
            if(left_b <= c):
                yield((a,b+left_b,c-left_b),left_b)
            if(left_b > c):
                yield((a, b+c, 0),c)



