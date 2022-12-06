# Parse parse parse...
    # Each stack will behave like, well, a stack. Implemented as a list
    # 9 Lists total

def make_stacks(filename):
    with open(filename) as file:
        initial = [line for line in file]
    stacks = []
    num_stacks = len(initial[-1].split('   '))

    for i in range(num_stacks):
        current_stack = []
        next_row = len(initial)-2
        next_addition = initial[next_row][1 + (i*4)]

        while next_addition != ' ':
            current_stack.append(next_addition)
            next_row -= 1
            try: # IndexError if it has reached the top of the file and there are no rows before it, probably a more better way to handle this
                next_addition = initial[next_row][1 + (i*4)]
            except IndexError:
                break

        stacks.append(current_stack)
    return stacks

def get_instructions(filename):
    with open(filename) as file:
        return [line.strip() for line in file]

def perform(stacks, instruction):
    instruction = instruction.split(" ")
    for _ in range(int(instruction[1])):
        stacks[int(instruction[5])-1].append(stacks[int(instruction[3])-1].pop())

def perform_part_2(stacks, instruction):
    instruction = instruction.split(" ")
    to_be_moved = []

    for _ in range(int(instruction[1])):
        to_be_moved.append(stacks[int(instruction[3])-1].pop())
    to_be_moved.reverse()

    stacks[int(instruction[5])-1] += to_be_moved

def main():
    stacks = make_stacks('day5/initial_stacks.txt')
    instructions = get_instructions('day5/instructions.txt')
    
    for instruction in instructions:
        #perform(stacks, instruction) 
        perform_part_2(stacks, instruction)
        #print('Done!!!')

    for stack in stacks:
        print(stack.pop())

if __name__ == "__main__":
    main()