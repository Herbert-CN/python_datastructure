"""
In a gold mine grid of size m * n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position you can walk one step to the left, right, up or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.


Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.
Example 2:

Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.


Constraints:

1 <= grid.length, grid[i].length <= 15
0 <= grid[i][j] <= 100
There are at most 25 cells containing gold.
"""
from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        biggest = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] != 0:
                    visited, results = set(), []
                    self.findPath(row, col, visited, 0,  results, grid)
                    if max(results) > biggest:
                        biggest = max(results)
        return biggest

    def findPath(self, row, col, visited, curGold, result, grid):
        if grid[row][col] == 0 or (row, col) in visited:  # 判断cell 是否可以访问
            return False

        # 访问该cell
        visited.add((row, col))
        curGold += grid[row][col]

        # 移动一步，访问相邻结点
        if (row > 0 and self.findPath(row-1, col, visited, curGold, result, grid))\
                or (col > 0 and self.findPath(row, col-1, visited, curGold, result, grid))\
                or (row < len(grid) -1 and self.findPath(row+1, col, visited, curGold, result, grid))\
                or (col < len(grid[row]) -1 and self.findPath(row, col+1, visited, curGold, result, grid)):
            return True  # 邻居结点能访问则继续访问
        else:
            result.append(curGold)
            visited.remove((row, col))
            curGold -= grid[row][col]
            return False # 所有相邻结点都不能访问


if __name__ == '__main__':
    test = Solution()
    # grid = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
    grid = [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]
    print(test.getMaximumGold(grid))