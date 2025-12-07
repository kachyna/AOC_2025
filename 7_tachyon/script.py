from collections import defaultdict

# We keep track of each beam and go one by one on coordinate y.
# If we see a beem hit a splitter, we double the beam for the next round.
# Because we use set to keep track of the beams, there will be no duplicates
def count_splits(grid):
    H = len(grid)
    W = len(grid[0])

    beams = {(grid[0].index('S'), 1)}
    splits = 0

    while beams:
        next_beams = set()

        for x, y in beams:
            ny = y + 1

            # if beam falls out of the grid
            if ny >= H: continue

            cell = grid[ny][x]

            # The beam splits and creates two new beams, one on the right and the other on the left
            if cell == '^':
                splits += 1
                if x - 1 >= 0: next_beams.add((x - 1, ny))
                if x + 1 < W: next_beams.add((x + 1, ny))
            
            # All other symbols we assume to be free spaces
            else: next_beams.add((x, ny))

        beams = next_beams

    return splits

def count_timelines(grid):
    H = len(grid)
    W = len(grid[0])

    # active[(x, y)] = how many timelines active at given position
    active = {(grid[0].index('S'), 1): 1}
    finished = 0 

    while active:
        new_active = defaultdict(int)
        for (x, y), count in active.items():
            ny = y + 1

            if ny >= H:
                finished += count
                continue

            cell = grid[ny][x]

            # Each line is split
            if cell == '^':
                if x - 1 >= 0: new_active[(x - 1, ny)] += count
                if x + 1 < W: new_active[(x + 1, ny)] += count
            # The line just moves down
            else: new_active[(x, ny)] += count

        active = new_active
    return finished

with open("test.txt") as f:
    lines = [list(line.strip()) for line in f.readlines()]
print (count_splits( lines ))

with open("test.txt") as f:
    lines2 = [list(line.strip()) for line in f.readlines()]
print (count_timelines( lines2 ))