
class Solution:
    def permutation(self, s: str):
        visited = set()
        result, subset = [], []
        self.backtracking(result, visited, subset, s)
        return result

    def backtracking(self, result, visited, subset, s):
        if len(subset) == len(s):
            result.append(subset)

        for ch in s:
            if ch not in visited:
                visited.add(ch)
                self.backtracking(result, visited, subset + [ch], s)
                visited.remove(ch)



if __name__ == '__main__':
    test = Solution()
    result_final = test.permutation("a1b2")
    print(result_final)


