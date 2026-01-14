def findPath(maze, pos, table=[]):
 # Step 1: Check if out of bounds
    if pos[0] < 0 or pos[1] < 0 or pos[0] >= len(maze) or pos[1] >= len(maze[0]) :
        return False
 
 # Step 2: Check if the current position is walkable
    if maze[pos[0]][pos[1]] == 1 :
        maze[pos[0]][pos[1]] = 0 #(Fill in the condition)
    # Step 3: Check if this is the goal
        if pos[0] == len(maze) - 1 and pos[1] == len(maze[0]) - 1:
            table.insert(0, (pos[0], pos[1]))
            return table
 # Step 4: Try moving **down** first
        if findPath(maze, (pos[0] + 1, pos[1]), table) != False:
            table.insert(0, (pos[0], pos[1]))
            return table

 # Step 5: Try moving **right**
        elif findPath(maze, (pos[0], pos[1] + 1), table) != False:
            table.insert(0, (pos[0], pos[1]))
            return table
        
        elif findPath(maze, (pos[0], pos[1] - 1), table) != False: #left
            table.insert(0, (pos[0], pos[1]))
            return table
        
        elif findPath(maze, (pos[0] - 1, pos[1]), table) != False: #top
            table.insert(0, (pos[0], pos[1]))
            return table
        return False
    else:
        return False
    
maze = [
 [1, 0, 1, 1, 1],
 [1, 1, 1, 0, 1],
 [0, 0, 1, 0, 1],
 [1, 1, 1, 0, 1],
 [1, 0, 0, 0, 1]
]
solution = findPath(maze, (0,0))
if solution:
    print("Solution Path: ", solution)
    for i in solution:
        maze[i[0]][i[1]] = "*"
    print("Maze with Solution Path")
    for row in maze:
        for cell in row:
             print(cell, end=' ')
        print()
else:
    print("No solution exists for the maze.")