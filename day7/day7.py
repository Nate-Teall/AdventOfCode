# Uhhhh, shit.
# So I need a way to represent the directory structure...
    # Possible with a list of lists?
        # outermoust list is / (following example)
        # the two inside are a and d
        # e is the list within the a
        # the letters are the files
        # [[f,g,h,[i]], [j, d, k]]
        # To get the size just go through each file within that list?
    # A dict probably better:
        # {/:{a:{e:{i:123}, f:123, g:123, h:123}, d:{j:123, d:123, k:123}}}
        # Probably best way of doing it
    # Well I tried my VERY BEST to implement the above, but I'm dumb lol
        # I created a directory class that behave like a node 

class Directory:
    __slots__ = ['__children', '__parent','__name', '__size']

    def __init__(self, parent, name):
        # Parent will be another directory object, None if /
        self.__parent = parent
        # The files and their sizes
        self.__children = {}
        self.__name = name
        self.__size = 0

    def add_child(self, name):
        self.__children[name] = Directory(self, name)

    def get_child(self, name):
        return self.__children[name]
    def get_children(self):
        return self.__children

    def increase_size(self, file):
        self.__size += file

    def get_total_size(self):
        # Recursion ???? ?? ? ? 
        # kill me :)
        total_size = 0
        for child in self.__children:
            total_size += self.__children[child].get_total_size()
        return total_size + self.__size

    def get_parent(self):
        return self.__parent
    
    def __str__(self):
        return self.__name

def try_this_shit_again_lol(input, current_directory):
    # I THINK THIS IS RIGHT??
    # How do I print this information..?
    for line in input:
        line = line.split(' ')

        if line[1] == 'cd' and line[2] != '..':
            current_directory = current_directory.get_child(line[2])

        elif line[0].isnumeric():
            current_directory.increase_size(int(line[0]))

        elif line[0] == 'dir':
            current_directory.add_child(line[1])
        
        elif line[1] == 'cd' and line[2] == '..':
            current_directory = current_directory.get_parent()

def print_directories(parent:Directory):
    print(parent, parent.get_total_size())
    if parent.get_total_size() < 100000:
        print("\t\t\tWOOOOOO")
    for child in parent.get_children():
        print_directories(parent.get_child(child))

def count_dirs(parent:Directory, total=0):
    # Now we can *actually* answer the question
    # I could have easily created (using recursion) a global dictionary mapping the name to it's size, and use that for part 1 and 2
        # But let's practice recursion instead
    for child in parent.get_children():
        total = count_dirs(parent.get_child(child), total)
    if parent.get_total_size() < 100000:
        total += parent.get_total_size()
    return total

def find_deletion(parent:Directory, minimum, current_smallest):
    if minimum < parent.get_total_size() < current_smallest:
        current_smallest = parent.get_total_size()
    for child in parent.get_children():
        current_smallest = find_deletion(parent.get_child(child), minimum, current_smallest)
    return current_smallest

def main():
    with open('day7/part1.txt') as file:
        input = [line.strip() for line in file]

    start = Directory(None, 'start')
    start.add_child('/')

    try_this_shit_again_lol(input, start)

    print_directories(start)
    # Thanks to this print statement, I can see that the total space used (size of /) is:
    # 44795677
    # 70000000 - 44795677 = 25204323 <- Free Space
    # 30000000 - 25204323 = 4795677 <- Space needed to be freed
    # Should I be doing this via code? Eh, nah
    print(count_dirs(start))
    print(find_deletion(start, 4795677, 70000000))


if __name__ == "__main__":
    main()
