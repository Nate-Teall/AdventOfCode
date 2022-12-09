def main():
    with open('day9/input.txt') as file:
        instructions = [line.strip() for line in file]
    
    # Okay okay, for some reason having the starting
    Tpos = [10000, 10000]
    Hpos = [10000, 10000]
    visited = set()
    visited.add(f"{Tpos[0]}{Tpos[1]}")

    for instruction in instructions:
        for _ in range(int(instruction[2])):
            if instruction[0] == 'R':
                Hpos[0] += 1

                if Hpos[0] - Tpos[0] >= 2:
                    Tpos[0] += 1 
                    Tpos[1] = Hpos[1] # This will make it move diagonally if necessary

            elif instruction[0] == 'L':
                Hpos[0] -= 1

                if Tpos[0] - Hpos[0] >= 2:
                    Tpos[0] -= 1 
                    Tpos[1] = Hpos[1]

            elif instruction[0] == 'U':
                Hpos[1] += 1

                if Hpos[1] - Tpos[1] >= 2:
                    Tpos[1] += 1 
                    Tpos[0] = Hpos[0]

            else:
                Hpos[1] -= 1

                if Tpos[1] - Hpos[1] >= 2:
                    Tpos[1] -= 1 
                    Tpos[0] == Hpos[0]

            print(f"{Tpos[0]} {Tpos[1]}\t{Hpos[0]} {Hpos[1]} ({instruction[0]})")
            visited.add(f"{Tpos[0]}{Tpos[1]}")
    print(len(visited))

if __name__ == "__main__":
    main()