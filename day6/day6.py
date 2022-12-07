def find_marker(stream):
    for i in range(14, len(stream)):
        code = stream[i-14:i]

        if len(set(code)) == 14:
            print(code, i)
            return
    
def main():
    with open('day6/part1.txt') as file:
        stream = [line for line in file]

    find_marker(stream[0])

if __name__ == "__main__":
    main()