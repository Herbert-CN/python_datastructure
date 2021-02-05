"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

You may return the answer in any order.



Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Example 2:

Input: n = 1, k = 1
Output: [[1]]


Constraints:

1 <= n <= 20
1 <= k <= n
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.dfs(list(range(1, n + 1)), k, [], result)
        return result

    def dfs(self, nums, k, path, result):
        if len(path) == k:
            result.append(path)
            return

        for i in range(len(nums)):
            self.dfs(nums[i + 1:], k, path + [nums[i]], result)


if __name__ == '__main__':
    test = Solution()
    print(test.combine(4, 2))