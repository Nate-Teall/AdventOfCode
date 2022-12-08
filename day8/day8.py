def is_visible(row, x, y, grid, val):
    # Visible from left?
    left = True
    for i in range(x-1,-1,-1):
        if row[i] >= val:
            left = False
            break

    # Visible from right?
    right = True
    for i in range(x+1, len(row)):
        if row[i] >= val:
            right = False
            break
    
    # Visible from top?
    top = True
    for i in range(y-1, -1, -1):
        if grid[i][x] >= val:
            top = False
            break
    
    # Visible from bottom?
    bottom = True
    for i in range(y+1, len(grid)):
        if grid[i][x] >= val:
            bottom = False
            break
    
    return bottom or top or left or right
    # I think this is kind of a backwards way of doing it, I should check if it is visible from one side, then immediately return True
    # However, the only way (I think) to check one side's visibility is by checking each tree to that side

def scenic_score(row, x, y, grid, val):
    left = 0
    for i in range(x-1,-1,-1):
        left+=1
        if row[i] >= val:
            break

    right = 0
    for i in range(x+1, len(row)):
        right+=1
        if row[i] >= val:
            break
    
    top = 0
    for i in range(y-1, -1, -1):
        top+=1
        if grid[i][x] >= val:
            break

    bottom = 0
    for i in range(y+1, len(grid)):
        bottom+=1
        if grid[i][x] >= val:
            break
        
    return bottom * top * left * right

def main():
    with open('day8/input.txt') as file:
        grid = [[char for char in line.strip()] for line in file]

    #print(len(grid)) # Rows: 99
    #print(len(grid[0])) # Cols: 99 

    visible = 392 # Visible from edges
    highest_score = 0
    for y in range(1, len(grid)-1):
        row = grid[y]
        for x in range(1,len(row)-1):
            score = scenic_score(row, x, y, grid, row[x])
            if score > highest_score:
                highest_score = score
            if is_visible(row, x, y, grid, row[x]):
                visible += 1
    print(visible)
    print(highest_score)


if __name__ == "__main__":
    main()