# ======== PART 1 ========

# takes a two dimensional array as an argument - each input row is split into numbers, creating a 2d array of numbers
def solve1( arr ):
    ret = 0
    # for every column of numbers, see what operation to do and execute it
    for col in range(0, len(arr[0])):
        if arr[-1][col] == "+":
            ret += sum( arr[x][col] for x in range(0, len(arr) - 1 ))
        elif arr[-1][col] == "*":
            acc = 1
            for x in range(0, len(arr) - 1) :
                acc = acc * arr[x][col]
            ret += acc
    return ret

# ======== PART 2 ========

#takes a one dimensional array containing strings as an argument 
def solve2( arr ):
    ret = 0
    # '+' for add, '*' for product, ' ' awaiting a new set of numbers
    mode = ' '
    acc = 1
    # for every character, even with the ending whitespace where we up the last acc if the number was a product
    for i in range(0, len(arr[0]) ):
        str_num = ''
        # if awaiting a new set of numbers, also take the new operand
        if mode == ' ' : mode = arr[-1][i]
        # create a string number
        for j in range(0, len(arr) - 1 ) :
            str_num += arr[j][i]
        
        #if it was all whitespace, we know we ended the set of numbers
        if str_num.strip() == '' :
            if mode == '*' :
                ret += acc
                acc = 1
            mode = ' '
            continue
        
        num = int(str_num)
        if mode == '+' : ret += num
        elif mode == '*' : acc *= num
    return ret

# ======== FUNCTION CALLS ========

with open("./input.txt") as f:
    arr = []
    for line in f.readlines():
        arr.append( line.split() )
for i in range(0, len(arr) - 1 ):
    arr[i] = list(map(int, arr[i]))
print( solve1(arr) )

with open("./input.txt") as f:
    arr = []
    for line in f.readlines():
        arr.append( line )
print( solve2(arr) )