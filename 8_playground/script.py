from math import *

# ========= COMMON FUNCTIONS =========

def calcDistance( p1, p2 ):
    return sqrt( ( p1[0] - p2[0] )**2 + ( p1[1] - p2[1] )**2 + ( p1[2] - p2[2] )**2 )

# ========= PART 1 =========
# Implementation with structure union-find:
# 1. Each point starts in its own set
# 2. Gradually, we merge the sets together
# 3. In the end, we find the largest 3 sets and return the sum of their sizes

# Union find structure where each point is represented by its original index
# The code has been inspired by the course AG1 taught at FIT CTU Prague, lecture 11
class unionFind:
    def __init__(self, size):
        self.parent = [-1 for _ in range(0, size)]
        self.depth = [1 for _ in range(0, size)]

    def find(self, e ):
        while( self.parent[e] ) != -1:
            e = self.parent[e]
        return e
    
    def union(self, e1, e2):
        a = self.find(e1)
        b = self.find(e2)
        if a == b : return False
        if self.depth[a] == self.depth[b]:
            self.depth[a] += 1
        if self.depth[a] < self.depth[b]:
            self.parent[a] = b
        if self.depth[a] > self.depth[b]:
            self.parent[b] = a
        return True
    
    def getUnionSizes(self):
        size = len(self.parent)
        ret = [ 0 for _ in range(0, size) ]
        for i in range(0, size ):
            idx = self.find(i)
            ret[ idx ] += 1
        return sorted(ret, reverse = True)

# Find distances between all points. This step is required because we only need to connect n closest points
# Returns an array of distances and indexes of the two points that create the distance
def getHeadLengths( points ):
    distances = []
    for i in range(0, len(points)):
        for j in range( i + 1, len(points) ):
            distances.append([ calcDistance( points[i], points[j] ), i, j])
    return distances

def solve1( input, n ):
    distances = sorted(getHeadLengths( input ))
    uf = unionFind( len(input) )
    i = 0

    for i in range(n):
        d, a, b = distances[i]
        uf.union( a, b )

    sizes = uf.getUnionSizes()
    return prod( sizes[:3]  )

# ========= PART 2 =========
def solve2( input ):
    distances = sorted(getHeadLengths( input ))
    uf = unionFind( len(input) )
    nbSets = len(input)
    i = 0

    for d, a, b in distances:
        if uf.union( a, b ):
            nbSets -= 1
        if nbSets == 1 : return input[a][0] * input[b][0]

# ========= FUNCTION CALLS =========

with open("input.txt") as f:
    lines = [ list(map(int, x.split(','))) for x in f.readlines()]

print(solve1(lines, 1000))
print(solve2(lines))