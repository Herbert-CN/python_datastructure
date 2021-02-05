"""
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.



Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
Example 3:

Input: n = 3, k = 1
Output: "123"


Constraints:

1 <= n <= 9
1 <= k <= n!
"""


class Solution:
    count = 0
    def getPermutation(self, n: int, k: int) -> str:
        return self.dfs(list(range(1, n+1)), [], k)


    def dfs(self, candidates, path, k):
        if len(candidates) == 0:
            self.count += 1
            if self.count == k:
                print(path)
                return path

        for i in range(len(candidates)):
            if self.count == k:
                break
            self.dfs(candidates[:i] + candidates[i + 1:], path + [candidates[i]], k)


if __name__ == '__main__':
    test = Solution()
    print(test.getPermutation(4, 9))
