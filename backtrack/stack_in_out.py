from typing import List


class Solution:
    def findAllResults(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.dfs(nums, 0, [], [], result)
        return result

    def dfs(self, nums, index, stack, path, result):
        if index == len(nums):
            temp1, temp2 = path.copy(), stack.copy()
            while temp2:
                temp1.append(temp2.pop())
            result.append(temp1)
            return

        self.dfs(nums, index+1, stack+[nums[index]], path, result)  # 入栈

        if stack:
            num = stack.pop()
            self.dfs(nums, index, stack, path+[num], result)

if __name__ == '__main__':
    test = Solution()
    print(test.findAllResults([1, 2, 3, 4]))