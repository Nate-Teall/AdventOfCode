def count_elves(filename):
    with open(filename) as file:
        elves = []
        current = 0

        for line in file:
            line = line.strip()

            if line == "":
                elves.append(current)
                current = 0
            else:
                current += int(line)
        
        # Add the last elf because lol
        elves.append(current)
        elves.sort(reverse=True)
        return elves

def main():
    result = count_elves("elves.txt")
    print(result[0] + result[1] + result[2])

main()