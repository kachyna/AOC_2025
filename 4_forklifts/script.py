import time

# CONSTANTS

MAX_ROLLS_AROUND = 4

# ======== COMMON FUNCTIONS ========

# Looks at all 8 positions around given index. Determines whether there is less than MAX_ROLLS_AROUND around it. 
def isAccessible( lines, x, y, max_x, max_y ):
    rollCount = 0
    # y 
    for j in range( y - 1, y + 2) :
        # x
        for i in range( x - 1, x + 2 ):
            # If we are out of bounds or in the middle of the eight positions, skip and don't add anything
            if ( i < 0 or i >= max_x or j < 0 or j >= max_y or ( i == x and j == y ) ) : continue
            if lines[j][i] == '@' : rollCount += 1 
            if rollCount >= MAX_ROLLS_AROUND : return False
    return True

# Removes roll in a strange way because Python strings are immutable
def removeRoll(lines, x, y) :
    str = lines[y][0:x] + '.' + lines[y][x+1:]
    return str

# ======== PART 1 ========

# Main loop for solvig. We look at each index, determine whether it is a roll and if so, whether it is accessible. 
def solve( lines ):
    max_x = len( lines[0].strip() )
    max_y = len( lines ) 
    ret = 0

    for y in range( 0 , max_y ):
        for x in range( 0 , max_x ):
            if lines[y][x] == '@' and isAccessible(lines, x, y, max_x, max_y) : ret += 1
    return ret

# ======== PART 2 ========

# Follows the structure of the previous part, only this time the loop is run until at least one change happened.
# Efficiency improvement: Instead of checking from the beginning in every iteration, we remember the most-left row and lowest collumn
# where change happened. During the next iteration, we start from most-left -1 and lowest - 1 (that is one higher).
# This saves some computing because it is not possible for a change to occur anywhere before these two.
def solve2( lines ):
    max_x = len( lines[0].strip() )
    max_y = len( lines ) 
    change = True

    # Note where the last change happened. -1 values default for no change.
    last_change_idx = [-1, -1] #row, col
    ret = 0

    while( change == True ) :
        change = False

        # We start at last change - 1, or 0 if change did not happened or happened at index zero.
        start_row = last_change_idx[0] - 1 if last_change_idx[0] > 0 else 0
        start_col = last_change_idx[1] - 1 if last_change_idx[1] > 0 else 0
        last_change_idx = [-1, -1]
        for y in range( start_col , max_y ):
            for x in range( start_row , max_x ):
                if lines[y][x] == '@' and isAccessible(lines, x, y, max_x, max_y) :
                    ret += 1
                    lines[y] = removeRoll( lines, x, y)
                    if (change == False ):
                        last_change_idx = [x, y]
                        change = True
                    else :
                        if ( last_change_idx[0] > x ) : last_change_idx[0] = x
                        if ( last_change_idx[1] > y ) : last_change_idx[1] = y
    return ret

# This algorithm could still be improved upon, because it might be pointless to iterate to end of the file again. 
# An ideal approach would probably be something inspired by BFS: We put all 8 indexes around the removed roll into stack and gradually 
# check whether they are good to remove, because they are the only ones that the change could have impacted.

def appendStack(lines, x, y, max_x, max_y, stack ) :
    for j in range( y - 1, y + 2) :
        for i in range( x - 1, x + 2 ):
            if ( i < 0 or i >= max_x or j < 0 or j >= max_y or ( i == x and j == y ) ) : continue
            # Append only rolls, no point in appending empty indexes
            if lines[j][i] == '@' : stack.append([i, j])
    return stack

def solve2_BFS( lines ):
    stack = []
    max = { "x" : len( lines[0].strip() ), "y" : len( lines ) } 
    ret = 0

    # At first, iterate through all rolls. Remove the ones that can be and fill the stack up with initial values.
    for y in range( 0 , max["y"] ):
        for x in range( 0 , max["x"] ):
            if lines[y][x] == '@' and isAccessible(lines, x, y, max["x"], max["y"]) :
                lines[y] = removeRoll( lines, x, y)
                stack = appendStack(lines, x, y, max["x"], max["y"], stack)
                ret += 1
    
    # Once the stack is filled with values, we can launch it.
    while( len(stack) != 0 ) :
        x, y = stack.pop()
        if lines[y][x] == '@' and isAccessible(lines, x, y, max["x"], max["y"]) :
            # If we remove a roll, we need to add it back all its neighbors to the stack again.
            lines[y] = removeRoll( lines, x, y)
            stack = appendStack(lines, x, y, max["x"], max["y"], stack)
            ret += 1
    
    return ret

# ======== RUN ========
with open("./input.txt") as f:
    lines = f.readlines()

print("The solution for part one is:", solve( lines ))

start_normal = time.time()
print("The solution for part two is:", solve2( lines ))
end_normal = time.time()
print (end_normal - start_normal, " seconds")

with open("./input.txt") as f:
    lines = f.readlines()


start_BFS = time.time()
print("The solution for part two with BFS is:", solve2_BFS( lines ))
end_BFS = time.time()
# From my tests on larger datasets, the BFS is generally 4 times faster than the iterative version. 
# In theory, BFS is O(m + n) while the iterative version is O(n^2).
print (end_BFS - start_BFS, " seconds")