"""
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.



Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]


Constraints:

10 <= low <= high <= 10^9
"""
from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        for i in range(len(str(low)), len(str(low(high)))+1):
            self.dfs(list(str(low)), list(str(high)), 0, i, [], result)
        print(result)

    def dfs(self, lowlist, highlist, index, curLength, path, result):
        if index > len(highlist):
            return

        if index == curLength:
            if int(''.join(path)) < int(''.join(highlist)):
                result.append(''.join(path))
            return

        if index == 0:
            if curLength == len(lowlist):
                for i in range(int(lowlist[index]), 10):
                    self.dfs(lowlist, highlist, index + 1, curLength, path + [str(i)], result)
            else:
                self.dfs(lowlist, highlist, index + 1, curLength, path + ['1'], result)

        else:
            if int(path[index-1]) + 1 < int(lowlist[index]) or int(path[index-1]) + 1 > 9:
                return
            else:
                self.dfs(lowlist, highlist, index+1, path+[str(int(path[index-1])+1)], result)



if __name__ == '__main__':
    test = Solution()
    test.sequentialDigits(100, 3000)



