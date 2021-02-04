from typing import List


class Solution:
    def findAllResults(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.dfs(nums, 0, [], [], result)
        return result

    def dfs(self, nums, index, stack, path, result):
        if index == len(nums):
            result.append(path+list(reversed(stack)))
            return

        self.dfs(nums, index+1, stack+[nums[index]], path, result)  # 入栈

        if stack:  # 出栈
            num = stack.pop()
            self.dfs(nums, index, stack, path+[num], result)

if __name__ == '__main__':
    test = Solution()
    print(test.findAllResults([1, 2, 3, 4, 5]))