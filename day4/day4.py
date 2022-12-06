# Given two ranges, one would fully contain the other if:
    # the beginning of one range is Greater Than (or Equal To) the beginning of the other AND
    # the end of the first range in Less Than the end of the other
# I had an issue where I wasn't changing from strings to integers, which goofed it up lol
def test_contain(range1, range2):
    return int(range1[0]) >= int(range2[0]) and int(range1[1]) <= int(range2[1])

# Given two ranges, one would overlap with the other if:
    # the end of the Lower Range is Greater Than or Equal to the beginning of the other range
        # the range is lower if the beginning of one is less than or equal to the beginning of the other
def test_overlap(range1, range2):
    if int(range1[0]) <= int(range2[0]):
        return int(range1[1]) >= int(range2[0])
    else:
        return test_overlap(range2,range1)

    # In hindsight, (hindsight being literally 30 seconds after finishing this, test_overlap could have been done by doing this test with both endpoints of a range)
    # Oh well lol
    # return range2[0] <= range1[0] <= range2[0]

def create_pairs():
    with open('day4/day4.txt') as file:
        pairs = [line.strip().split(',') for line in file]
    for pair in pairs:
        pair[0] = pair[0].split('-')
        pair[1] = pair[1].split('-')

    return pairs

def main():
    pairs = create_pairs()
    total_contains = 0
    total_overlaps = 0

    for pair in pairs:
        if test_contain(pair[0],pair[1]) or test_contain(pair[1],pair[0]):
            total_contains += 1 
        
        if test_overlap(pair[0], pair[1]):
            print(pair)
            total_overlaps += 1
    
    print(total_contains)
    print(total_overlaps)

if __name__ == "__main__":
    main()