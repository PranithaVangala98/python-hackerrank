def gridChallenge(grid):
    
    
    grid_list = [] 
    for i in range (0,len(grid)):
        x = list(grid[i])
        x.sort()
        grid_list.append(x)
        
    print(grid_list)
    y = len(grid_list)
    z = len(grid_list[0])
    for j in range (0,z):
        for i in range (0,y-1):
            if grid_list[i][j]> grid_list[i+1][j]:
                return "NO"
    return "YES"            
grid = ['abc','ade','efg']
print(gridChallenge(grid))

