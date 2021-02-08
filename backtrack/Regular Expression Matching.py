class Solution:
    matched = False
    def isMatch(self, s: str, p: str) -> bool:
        self.matched = False
        self.dfs(0, 0, list(p), list(s))
        return self.matched

    def dfs(self, pIndex, sIndex, pattern, strToMatch):
        if self.matched:
            return

        if pIndex == len(pattern):
            if sIndex == len(strToMatch):
                self.matched = True
            return

        if pattern[pIndex] == '.':  # pattern character is '.', it matches any character
            if pIndex < len(pattern)-1 and pattern[pIndex+1] == '*':
                for k in range(1, len(strToMatch) + 1 - sIndex):
                    self.dfs(pIndex+2, sIndex + k, pattern, strToMatch)
            else:
                self.dfs(pIndex + 1, sIndex + 1, pattern, strToMatch)  # jump and continue to compare next character
        elif strToMatch[sIndex] == pattern[pIndex]:  # common character and same
            letter = pattern[pIndex]
            if pIndex < len(pattern)-1 and pattern[pIndex+1] == '*':
                for k in range(1, len(strToMatch) + 1 - sIndex):
                    self.dfs(pIndex+2, sIndex + k, pattern, strToMatch)
            else:
                self.dfs(pIndex + 1, sIndex + 1, pattern, strToMatch)  # jump and continue to compare next character
        elif strToMatch[sIndex] != pattern[pIndex]:
            if pIndex < len(pattern) - 1 and pattern[pIndex + 1] == '*':
                self.dfs(pIndex + 2, sIndex, pattern, strToMatch)

if __name__ == '__main__':
    test = Solution()
    # print(test.isMatch("aa", "a"))
    # print(test.isMatch("aa", "a*"))
    # print(test.isMatch("ab", ".*"))
    # print(test.isMatch("aab", "c*a*b"))
    print(test.isMatch("ssippi", "s*p*."))