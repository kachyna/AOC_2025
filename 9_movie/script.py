def calculateArea( a, b ):
    return ( abs(a[0] - b[0]) + 1 ) * ( abs(a[1] - b[1]) + 1 ) 

with open("test.txt") as f:
    points = []
    for l in f.readlines():
        a,b = str(l).strip().split(',')
        points.append( [int(a), int(b)] )

res = []
for i in range( len(points) ):
    for j in range(len(points) ):
        if i >= j : continue
        res.append( calculateArea( points[i], points[j] ) )
    

print(sorted(res, reverse=True)[0])

# ======== PART 2 ===========

# The rectangle defined by a, b is only valid if all other red tiles
# that are connecting a, b have smaller (for the point with smaller coordinate),
# resp higher coordinates that points a, b.

def pointIsInGreen( x, a, b ):
    x_left = min( a[0], b[0] )
    x_right = max( a[0], b[0] )
    y_up = min( a[1], b[1] )
    y_bot = max( a[1], b[1] )

    # Assure that a is the smaller variable on x
    if ( a[0] > b[0]): a, b = b, a

    # if a has higher y (is lower on the grid)
    if a[1] > b[1]:
        if  ( x_left <= x[0] and x[0] <= x_right ) and \
            ( x[1] > y_up ) : return False
        
    if a[1] < b[1]:
        if  ( x_left <= x[0] and x_right <= b[0] ) and \
            ( x[1] < y_bot ) : return False

    # Is strictly within x and strictly within y
 
    return True

def findNext( x ):
    return points[points.index( x ) + 1]

def findPrevious( x ):
    return points[points.index( x ) - 1]

def rectangleIsWithinGreen( a, b ):
    if a[0] == b[0] or a[1] == b[1] : return True
    curr = a
    while curr != b:
        if not pointIsInGreen( curr, a, b ): return False
        curr = findNext( curr )

    curr = a
    while curr != b:
        if not pointIsInGreen( curr, a, b): return False
        curr = findPrevious( curr )
    return True

ret = 0
for i in range( len(points) ):
    for j in range(len(points) ):
        if i >= j : continue
        c = calculateArea( points[i], points[j] )
        if c < ret : continue
        if rectangleIsWithinGreen( points[i], points[j]): ret = c


print( ret )
    