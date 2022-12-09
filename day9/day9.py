def main():
    with open('day9/input.txt') as file:
        instructions = [line.strip() for line in file]
    
    # Okay okay, for some reason having the starting positions 0 vs 10000 changes the output? 
    # It should only be changing the positions of the head and tail, then adding that position to the set of positions visited by the tail
    # So, the starting point should be irrelevant? Maybe there are some odd shenanigans regarding negative numbers?
        # With this new solution, the answer is even less, and the starting points are still influencing it??
        # I'm so dumb... I'm only moving u/d/l/r a number of times based on the second index of the line. So double digit numbers aren't being counted properly... 
        # I still don't know why the issue with differing starting positions happened, but it works now ig?
    Tpos = [0, 0]
    Hpos = [0, 0]
    visited = set()
    visited.add(f"{Tpos[0]}{Tpos[1]}")

    # New Plan:
    # If the head goes too far away, simply set the tail's position to the head's current, then move the head

    for instruction in instructions:
        instruction = instruction.split(' ')
        for _ in range(int(instruction[1])):
            prev_H = [Hpos[0], Hpos[1]]

            if instruction[0] == 'R':
                Hpos[0] += 1

            elif instruction[0] == 'L':
                Hpos[0] -= 1

            elif instruction[0] == 'U':
                Hpos[1] += 1

            else:
                Hpos[1] -= 1

            if is_too_far(Hpos, Tpos):
                    Tpos = prev_H

            print(f"{Tpos[0]} {Tpos[1]}\t{Hpos[0]} {Hpos[1]} ({instruction[0]})")
            visited.add(f"{Tpos[0]}{Tpos[1]}")
    #print(visited)
    print(len(visited))


def is_too_far(Hpos, Tpos):
    return abs(Hpos[0] - Tpos[0]) >= 2 or abs(Hpos[1] - Tpos[1]) >= 2

if __name__ == "__main__":
    main()