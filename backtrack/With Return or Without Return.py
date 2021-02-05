"""
You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.



Example 1:

Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: tiles = "AAABBC"
Output: 188
Example 3:

Input: tiles = "V"
Output: 1


Constraints:

1 <= tiles.length <= 7
tiles consists of uppercase English letters.
"""

from typing import List


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        result = []

        def dfs(letters, path, result):
            if path:
                result.append(path)

            for i in range(len(letters)):
                if i > 0 and letters[i] == letters[i - 1]:
                    continue
                dfs(letters[:i] + letters[i + 1:], path + [letters[i]], result)

        letter_list = list(tiles)
        letter_list.sort()
        dfs(letter_list, [], result)
        return result

    def numTilePossibilities_v2(self, tiles: str) -> int:
        result = []

        def dfs(letters, path, result):
            if path:
                result.append(path)
                return

            for i in range(len(letters)):
                if i > 0 and letters[i] == letters[i - 1]:
                    continue
                dfs(letters[:i] + letters[i + 1:], path + [letters[i]], result)

        letter_list = list(tiles)
        letter_list.sort()
        dfs(letter_list, [], result)
        return result



if __name__ == '__main__':
    test = Solution()
    print(test.numTilePossibilities("CDC"))
    print(test.numTilePossibilities_v2("CDC"))