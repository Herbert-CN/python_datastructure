from typing import List


class Solution:
    def getAllResults(self, n: int) -> List[str]:
        result = []
        self.dfs(0, 2*n, [], result)
        return result

    def dfs(self, curBalance, n, path, result):
        if len(path) == n:
            if curBalance == 0:
                result.append(''.join(path))
            return
        if curBalance == 0:
            self.dfs(curBalance + 1, n, path + ['('], result)
        elif 0 < curBalance <= n - len(path):
            self.dfs(curBalance - 1, n, path + [')'], result)
            self.dfs(curBalance + 1, n, path + ['('], result)
        else:
            return

if __name__ == '__main__':
    test = Solution()
    print(test.getAllResults(1))