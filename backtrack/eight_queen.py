class Solution:
    count = 0
    def findQueen(self, size: int):
        grid = [[" " for _ in range(size)]for _ in range(size)]
        # self.helper(0, size, grid)
        self.helper_allSolution(0, size, grid)
        print("Count: ", self.count)
        return grid

    def helper(self, row, size, result):  # 寻找一种方案
        if row == size:
            print(result)
            return True

        for col in range(size):
            if self.backtracking_checking(row, col, result, size):
                result[row][col] = 'Q'
                if not self.helper(row+1, size, result):
                    result[row][col] = ' '
                else:
                    return True
        return False

    def helper_allSolution(self, row, size, result):  # 寻找一共有多少种方案
        if row == size:
            self.count += 1
            print(result)

        col = 0
        while col < size:
            if self.backtracking_checking(row, col, result, size):
                result[row][col] = 'Q'
                self.helper(row + 1, size, result)
                result[row][col] = ' '
            col += 1

        # for col in range(size):
        #     if self.backtracking_checking(row, col, result, size):
        #         result[row][col] = 'Q'
        #         if not self.helper_allSolution(row+1, size, result):
        #             result[row][col] = ' '
        #         else:
        #             pass

        # return False

    def backtracking_checking(self, row, column, result, size):
        """检查能否在row, column的位置上放置Q, 因为是逐行放置的所以只用检查row前面的行"""
        for i in range(row):  # 检查行
            if result[i][column] == 'Q':
                return False

        # 检查2个对角线, 左下角，右下角
        i = 1
        while row - i >= 0 and column - i >= 0:
            if result[row-i][column-i] == 'Q':
                return False
            i+=1

        i = 1
        while row + i < size and column - i >= 0:
            if result[row+i][column-i] == 'Q':
                return False
            i+=1

        return True



def queen(A, cur=0):
    if cur == len(A):
        print(A)
        return 0
    for col in range(len(A)):
        A[cur], flag = col, True
        for row in range(cur):
            if A[row] == col or abs(col - A[row]) == cur - row:
                flag = False
                break
        if flag:
            queen(A, cur+1)


if __name__ == '__main__':
    test = Solution()
    myresult = test.findQueen(8)

    # queen([None] * 8)