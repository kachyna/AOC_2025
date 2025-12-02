# =========== COMMON FUNCTIONS ===========

def parseLine( line ) :
    return line.split(",")

def is_prime(n):
    if n < 2:
        return False

    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    return sieve[n]


num = 31
print(is_prime(num))

# =========== PART 1 ===========

def hasTwoMatchingStrings( x ) :
    x_len = len(x)
    middle = int(x_len / 2)
    return x[0:middle] == x[middle:x_len]

def twoMatchingStrings( lower, upper ) :
    ret = 0

    # For every number x in range
    for x in range (int(lower), int(upper) + 1) :
        # Cannot have two matching strings if isn't divisible by two
        if len( str(x) ) % 2 != 0 : continue
        elif hasTwoMatchingStrings( str(x) ) : ret += x
    return ret

# =========== PART 2 ===========

# x is the number to be checked
# sub_len is the length of substring we are checking
def numberIsInvalid( x, sub_len ) :
    substringToMatch = x[:sub_len]
    idx_l = 0
    idx_r = sub_len

    while idx_r <= len(x) :
        if substringToMatch != x[idx_l:idx_r] : return False
        else :
            idx_l = idx_r
            idx_r += sub_len
    return True

def countInvalid( lower, upper ) :
    ret = 0

    # For every number x in range
    for x in range (int(lower), int(upper) + 1) :
        x_len = len( str(x) )

        # If len of x is prime, there cannot be any matching substrings of length > 1 (as it is not divisible),
        # therefore we can skip it while checking just for sub_len 1
        if is_prime(x_len) : 
            if numberIsInvalid( str(x), 1) : ret += x
            continue

        # For all lengths of substrings
        for sub_len in range(1, int( x_len / 2 ) + 1 ) :

            # If length of x is not divisible by substring length, we cannot split it into same-length substrings
            if x_len % sub_len != 0 : continue
            
            # Otherwise check whether the number is invalid. If so, add it up to ret.
            # It is necessarry to break after because numbers like 111111 would have added up multiple times.
            elif numberIsInvalid( str(x), sub_len) :
                ret += x
                break
    
    return ret
            
# =========== SCRIPT ===========
with open("./input.txt", "r") as f:
    data = parseLine( f.readline() )

# =========== PART 1 ===========
res = 0
for ran in data:
    split = ran.split("-")
    res += twoMatchingStrings( split[0], split[1] )
print("The result #1 is", res)

# =========== PART 2 ===========

res2 = 0
for ran in data:
    split = ran.split("-")
    res2 += countInvalid( split[0], split[1] )
print("The result #2 is", res2)