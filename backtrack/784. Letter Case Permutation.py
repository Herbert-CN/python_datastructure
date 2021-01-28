"""
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. You can return the output in any order.



Example 1:

Input: S = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: S = "3z4"
Output: ["3z4","3Z4"]
Example 3:

Input: S = "12345"
Output: ["12345"]
Example 4:

Input: S = "0"
Output: ["0"]


Constraints:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.
"""
from typing import List

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        self.res=[]
        self.dfs(S,'',0)
        return self.res

    def dfs(self, S, subStr, index):
        if index==len(S):
            self.res.append(subStr)
            return

        if S[index].isalpha():
            self.dfs(S,subStr+S[index].lower(),index+1)
            self.dfs(S,subStr+S[index].upper(),index+1)
        else:
            self.dfs(S,subStr+S[index],index+1)


class Solution2:
    def letterCasePermutation(self, S: str) -> List[str]:
        result = []
        self.helper(0, "", result, S)
        return result

    def helper(self, index, subStr, result, S):
        if len(subStr) == len(S):
            result.append(subStr)
            return

        for ch in S:
            if ch.isalpha():
                self.helper(index + 1, subStr + ch.lower(), result, S)
                self.helper(index + 1, subStr + ch.upper(), result, S)
            else:
                self.helper(index + 1, subStr + ch, result, S)

if __name__ == '__main__':
    test = Solution()
    print(test.letterCasePermutation("a1b2"))



