def find_dupe(rucksack):
    # I will presume all rucksacks have even # of items
    comp_size = int(len(rucksack)/2)
    compartment1 = set(rucksack[:comp_size])
    compartment2 = set(rucksack[comp_size:])

    for element in compartment1:
        if element in compartment2:
            return element

def intersection(sack1, sack2, sack3):
    for item in sack1:
        if item in sack2 and item in sack3:
            return item

def find_priorities(list):
    total = 0 
    for item in list:
        if item.islower():
            total += ord(item) - 96
        else:
            total += (ord(item) - 64) + 26
    return total

def main():
    with open('day3/day3.txt') as file:
        rucksacks = [line.strip() for line in file]

    dupes = []
    for rucksack in rucksacks:
        dupes.append(find_dupe(rucksack))

    total_dupes = find_priorities(dupes)
    print(total_dupes)

    # Part 2
    # The hardest part about today was definitely splitting the stacks into groups.
    # I just couldn't think of an easy way to do this tbh. 
        # I think enumerate would've helped with this, I should learn how to use that function
    # However I do think the helper functions helped solve the problem in a clean way

    groups = []
    with open('day3/day3.txt') as file:
        current_group = []      
        num = 0

        for line in file:
            if num == 3:
                groups.append(current_group)
                current_group = []
                num = 0

            current_group.append(line.strip())
            num += 1
        
        groups.append(current_group)

    badges = []
    for group in groups:
        badges.append(intersection(group[0],group[1],group[2]))
    
    total_badges = find_priorities(badges)
    print(total_badges)

if __name__ == "__main__":
    main()