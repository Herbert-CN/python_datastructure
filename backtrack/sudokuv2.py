class Solution:
    grid = [[None for _ in range(9)] for _ in range(9)]

    def solve(self):
        cell = self.getNoneCell()
        if not cell:  # cell is None and all cells have value
            return True
        else:
            row, col = cell
        for value in range(1, 10):
            if self.isValid(row, col, value):
                self.grid[row][col] = value

                if self.solve():
                    return True

                self.grid[row][col] = None

        return False


    def getNoneCell(self):
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] is None:
                    return row, col
        return None


    def isValid(self, row, col, value):  # Check if value valid for row, col
        for i in range(9): # check row
            if self.grid[i][col] == value:
                return False
        for i in range(9):  # check column
            if self.grid[row][i] == value:
                return False
        m, n = row//3, col//3  # check palace
        for i in range(3):
            for j in range(3):
                if self.grid[3*m+i][3*n+j] == value:
                    return False
        return True

    def updateGrid(self, row, col, value):
        self.grid[row][col] = value




if __name__ == '__main__':
    test = Solution()
    test.updateGrid(0, 5, 9)
    test.updateGrid(0, 6, 2)
    test.updateGrid(1, 1, 1)
    test.updateGrid(1, 5, 4)
    test.updateGrid(1, 6, 8)
    test.updateGrid(2, 2, 6)
    test.updateGrid(2, 3, 5)
    test.updateGrid(2, 7, 7)
    test.updateGrid(2, 8, 3)
    test.updateGrid(3, 2, 9)
    test.updateGrid(3, 3, 8)
    test.updateGrid(3, 8, 4)
    test.updateGrid(5, 0, 7)
    test.updateGrid(5, 1, 5)
    test.updateGrid(5, 5, 3)
    test.updateGrid(5, 6, 6)
    test.updateGrid(6, 0, 4)
    test.updateGrid(6, 1, 8)
    test.updateGrid(6, 5, 6)
    test.updateGrid(6, 6, 5)
    test.updateGrid(7, 2, 2)
    test.updateGrid(7, 3, 7)
    test.updateGrid(7, 7, 9)
    test.updateGrid(8, 2, 3)
    test.updateGrid(8, 3, 1)

    # print(test.grid)

    test.solve()
    print(test.grid)