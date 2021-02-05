"""
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.



Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations. [1,2,1] is not valid because 1 is used twice.
Example 4:

Input: k = 3, n = 2
Output: []
Explanation: There are no valid combinations.
Example 5:

Input: k = 9, n = 45
Output: [[1,2,3,4,5,6,7,8,9]]
Explanation:
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
There are no other valid combinations.


Constraints:

2 <= k <= 9
1 <= n <= 60
"""
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        self.dfs(k, n, [], result, list(range(1, 10)))
        return result

    def dfs(self, k, n, path, res, candidates):
        if n < 0 or k < 0:
            return

        if n == 0 and k == 0:
            res.append(path)

        for i in range(len(candidates)):
            self.dfs(k-1, n-candidates[i], path+[candidates[i]], res, candidates[i+1:])


    # def helper(self, k, n, visited, res):
    #     if n < 0 or k < 0:
    #         return
    #
    #     if n == 0 and k == 0:
    #         res.append(list(visited))
    #         return
    #
    #     for i in range(1, 10):
    #         if i not in visited:
    #             visited.add(i)
    #             self.helper(k - 1, n - i, visited, res)
    #             visited.remove(i)

if __name__ == '__main__':
    test = Solution()
    # assert test.combinationSum3(9, 45) == [[1,2,3,4,5,6,7,8,9]]
    # print(test.combinationSum3(3, 9))
    print(test.combinationSum3(9, 45))