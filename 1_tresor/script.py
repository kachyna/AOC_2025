# ======= CONSTANTS ========

FILE_PATH = "./input.txt"
START_POS = 50

# ======= COMMON FUNCTIONS ========

# Takes line in the file as a parameter.
# Converts line into an integer which is positive for R and negative for L.
def prepare( line ) :
    return int(line[1:]) if line[0] == "R" else - int(line[1:])

# Uses modular arithmetic to determine the next position after turning amount of times (negative for L direction).
def turn( curr, amount ) :
        return ( curr + int(amount) ) % 100
    
# ======= PART ONE ========

# For each line, use function turn. If the resulting position ends up being zero, add one to counter.
def part1( file ):
    pos = START_POS
    ret = 0
    for line in file.readlines():
        pos = turn( pos, prepare(line) )
        if (pos == 0 ) : ret += 1
    return ret
    
# ======= PART TWO ========

# Calculates whole_rotations, which are always multiples of 100.
# One whole rotation means that that it surely crosses zero and ends up in the same spot.
# After that, calculate wheter the remainder of amount position_change (always < 99) passes zero.
# If so, return 1 + whole rotations.
def nb_crosses_zero( curr, amount ) :

    whole_rotations = abs ( int(amount / 100) )
    position_change = abs( amount ) % 100
    if ( amount < 0 ) : position_change = - position_change

    #If already starting at zero, position_change (which is < 99) will never give a full turn. Hence return only whole_rotations.
    if ( curr == 0 ) : return whole_rotations

    if curr + position_change >= 100 or curr + position_change <= 0: 
        return 1 + whole_rotations
    else : return whole_rotations

# Launch a loop which calls turn and does a summaiton of nb_crosses_zero
def part2( file ):
    pos = START_POS
    ret = 0
    for line in file.readlines():
        amount = prepare(line)
        ret += nb_crosses_zero( pos, amount )
        pos = turn( pos, amount )
    return ret

# ====== SCRIPT =======

f = open(FILE_PATH)
print("The number of times the head POINTS TO zero is: ", part1( f ))

f.seek(0)
print("The number of times the head CROSSES zero is: ", part2( f ))

f.close()





    
