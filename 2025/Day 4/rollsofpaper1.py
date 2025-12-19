def fileProcess(filename):
    grid = []

    #Open the file to read inside
    with open(filename, 'r', encoding="utf-8") as file:
        
        for lineNum, line in enumerate(file, start=1):
            bank = line.strip()
            if not bank: continue #skip empty line

            grid.append(bank)

            print(f"Line {lineNum}: {bank}")

    return grid

#First part: Rolls of paper can be accessed by a forklift.
def checkRolls(grid):
    rows = len(grid)
    cols = len(grid[0])
    result = [list(row) for row in grid]
    accessibleCount = 0

    #Possible neighbir positions around a cell
    #Top-left,      top,   top right
    #   left               right
    #bottom-left, bottom, bottom-right
    direction = [(-1, -1), 
                 (-1, 0), 
                 (-1, 1),
                 (0, -1), 
                 (0, 1), 
                 (1, -1), 
                 (1, 0), 
                 (1, 1)]
    
    # loop through the grid
    for i in range(rows):
        for j in range(cols):

            # if it's a roll, check the neightbor coordinates
            if grid[i][j] == "@":
                count = 0 # for counting neighbors

                for dx, dy in direction: # check all 8 neighbors
                    ni, nj = i + dx, j + dy

                    # stay inside of the grid boundaries
                    if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == "@":
                        count += 1

                #if x is less than 4 neighbors
                if count < 4:
                    result[i][j] = 'x'
                    accessibleCount += 1

    #update the grid and total number of accessible rolls
    return [''.join(row) for row in result], accessibleCount
    
def removeRolls(grid):
    rows = len(grid)
    cols = len(grid[0])
    result = [list(row) for row in grid]
    removed = 0
    changed = True

    #Possible neighbir positions around a cell
    #Top-left,      top,   top right
    #   left               right
    #bottom-left, bottom, bottom-right
    direction = [(-1, -1), 
                 (-1, 0), 
                 (-1, 1),
                 (0, -1), 
                 (0, 1), 
                 (1, -1), 
                 (1, 0), 
                 (1, 1)]
    
    while changed:
        changed = False
        toRemove = []

        # Find accessible rolls
        for i in range(rows):
            for j in range(cols):

                # if it's a roll, check the neightbor coordinates
                if result[i][j] == "@":
                    count = 0 # for counting neighbors

                    for dx, dy in direction: # check all 8 neighbors
                        ni, nj = i + dx, j + dy

                        # stay inside of the grid boundaries
                        if 0 <= ni < rows and 0 <= nj < cols and result[ni][nj] == "@":
                            count += 1

                    if count < 4:
                        toRemove.append((i, j))

        #Remove the accessible rolls
        if toRemove:
            changed = True
            for i, j in toRemove:
                result[i][j] = "." #Mark removed

                removed +=1
    return [''.join(row) for row in result], removed

solution = fileProcess("day4.txt")

#First part
outputGrid, totalAccessible = checkRolls(solution)

print("\nGrid:")
for row in outputGrid:
    print(row)

print(f"Total accessible rolls: {totalAccessible}")

#Second part
finalGrid, totalRemoved = removeRolls(solution)

print("\nGrid: ")
for row in finalGrid:
    print(row)

print(f"Total rolls removed: {totalRemoved}")