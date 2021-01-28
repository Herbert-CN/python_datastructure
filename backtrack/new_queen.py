class Solution:
    count = 0
    grid = [[" " for _ in range(8)] for _ in range(8)]
    result = []

    def findQueen(self, curRow: int):
        if curRow == 8:
            self.count += 1
            self.printQueen()
            self.result.append(self.grid)
            return

        for col in range(8):
            if self.isValid(curRow, col):
                self.grid[curRow][col] = 'Q'
                self.findQueen(curRow+1)  # 可以在这里进行处理，搜寻返回一个结果
                self.grid[curRow][col] = ' '

    def isValid(self, row, col):
        for i in range(row):  # 检查行
            if self.grid[i][col] == 'Q':
                return False

        # 一定要注意实际的grid 对应的坐标系映射的问题，困扰很久
        i = 1
        while row - i >= 0 and col - i >= 0:
            if self.grid[row - i][col - i] == 'Q':
                return False
            i += 1

        i = 1
        while row - i >= 0 and col + i < 8:
            if self.grid[row - i][col + i] == 'Q':
                return False
            i += 1

        return True

    def printQueen(self):
        print(self.grid)
        # print("=======================" * 5)
        # for line in self.grid:
        #     print(line)
        # print("=======================" * 5)
if __name__ == '__main__':
    test = Solution()
    test.findQueen(0)
    print(test.count)