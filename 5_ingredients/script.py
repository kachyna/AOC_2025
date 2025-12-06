# ========= GENERAL FUNCTIONS =========

def parse(f) :
    ranges = []
    ingredients = []
    line = f.readline()
    while (line != '\n'):
        ranges.append(line.strip())
        line = f.readline()

    for line in f.readlines():
        ingredients.append(line.strip())
    return ranges, ingredients

def createRanges(ranges):
    intervals = []
    for r in ranges:
        lower, upper = r.split('-')
        intervals.append((int(lower), int(upper)))

    # Sort by start
    intervals.sort()

    merged = []
    start, end = intervals[0]

    for s, e in intervals[1:]:
        if s <= end + 1:  # intersects or touches
            end = max(end, e) # extend the interval with the higher value
        else: # if does not intersect nor touch
            merged.append((start, end)) # end this interval by adding it to the array
            start, end = s, e # mark its values as new reference
    # add the last interval into the array
    merged.append((start, end))

    return merged


# ========= PART 1 =========

def countFreshIngredients( ranges, ingredients ):
    ret = 0
    ran = createRanges( ranges )
    for i in ingredients:
        for r in ran:
            s, e = r
            if s <= int(i) and int(i) <= e :
                ret +=1
                break
    return ret

# ========= PART 2 =========

def countAllFreshIngredients( ranges ):
    ret = 0
    ran = createRanges( ranges )
    return sum(e - s + 1 for s, e in ran)

# ========= FUNCTOIN CALLS =========

with open("./input.txt") as f:
    ranges, ingredients = parse(f)

print(countFreshIngredients(ranges, ingredients))
print(countAllFreshIngredients(ranges))
