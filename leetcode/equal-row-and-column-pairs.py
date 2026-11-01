class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
      
        gridMap = {}
        for i in grid:
            i = tuple(i)
            if i in gridMap:
                gridMap[i] +=1 
            else:
                gridMap[i] = 1
        
        count = 0
        for c in range(len(grid)):
            colList = []
            for r in range(len(grid)):
                colList.append(grid[r][c])
            colList = tuple(colList)
            if colList in gridMap:
                count += gridMap[colList]
        return count