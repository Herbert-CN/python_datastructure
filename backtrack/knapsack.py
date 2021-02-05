"""
艺术品 - 重量 - 价值
1 - 2 - 3
2 - 3 - 4
3 - 4 - 8
4 - 5 - 8
5 - 9 - 10

背包最大能装20，求最大值
"""
from typing import List, Tuple

class Solution:
    def findMaxValue(self, arts: List[Tuple[int, int]], capacity: int) -> int:
        maxValue = 0

        def dfs(arts, capacity, curValue):
            nonlocal maxValue

            if capacity < 0:
                return
            elif curValue > maxValue:
                maxValue = curValue

            for i in range(len(arts)):
                dfs(arts[i+1:], capacity-arts[i][0], curValue + arts[i][1])

        dfs(arts, capacity, 0)

        return maxValue


if __name__ == '__main__':
    test = Solution()
    arts = [(2, 3), (3, 4), (4, 8), (5, 8), (9, 10)]
    print(test.findMaxValue(arts, 20))