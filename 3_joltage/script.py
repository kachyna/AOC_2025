
# ============== SOLUTION ==============

# Helper function for determining whether given cipher is larger than line input at pos x
def isMax( line, x, arr, cipher ) :

    # If cipher at input position x is larger than currently saved highest cipher
    if int(line[x]) > int(arr[cipher]) :
        return True

# Takes input line and number length as argument. Can be used to solve both parts (num_len = 2 for the first part, num_len = 12 for the second)
def findNumber( line, num_len ) :

    # Position at which we will start the next iteration of finding the largest cipher as it makes no sense to go from the beginning every time.
    next_position = 0
    # Initialize an array of num_len zeros for saving highest ciphers
    arr = [0] * num_len      

    # We need to collect num_len ciphers, therefore we loop over the input num_len times
    for cipher in range(0, num_len) :
          
          # From the cipher that follows the highest previous one, loop through each number to find the next highest cipher
          # Stop at num_len - cipher + 1 - we cannot go the end with every cipher as it is needed to save space for following ciphers
          for x in range(next_position, len(line) - ( num_len - cipher ) + 1) :

            # If we find a max, write it to the array at corresponding cipher position
            if isMax( line, x, arr, cipher ) :
                arr[cipher] = line[x]
                next_position = x + 1

            # If we find a 9, we know there won't be any higher valued cipher and we can go for the next cipher
            if line[x] == '9' : break

    # Concat the string, and return its int value
    ret = str('')
    for c in range(0, num_len) :
        ret += arr[c]
    return int(ret)

# Loops over each line and adds up the results
def solve( lines, num_len ) :
    ret = 0
    for line in lines:
        ret += findNumber( line.strip(), num_len )
    return ret
        
# ================ RUN =================

with open("./input.txt") as f:
    lines = f.readlines()

print("Part one solution:", solve( lines, 2 ))
print("Part two solution:", solve( lines, 12 ))