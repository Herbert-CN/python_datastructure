"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.



Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]


Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self.dfs(candidates, target, [], result)
        return result

    def dfs(self, candidates: List[int], target: int, path: List[int], result: List[List[int]]) -> None:
        if target < 0:
            return
        if target == 0:
            result.append(path)
            return

        for index in range(len(candidates)):
            if index > 0 and candidates[index] == candidates[index - 1]:
                continue
            if candidates[index] > target:
                break
            else:
                self.dfs(candidates[index+1:], target-candidates[index], path+[candidates[index]], result)

if __name__ == '__main__':
    test = Solution()
    print(test.combinationSum2([10,1,2,7,6,1,5], 8))

    # print(test.combinationSum2([2, 5, 2, 1, 2], 5))

