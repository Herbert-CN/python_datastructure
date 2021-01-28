"""
Version 1
"""

from typing import List


class Solution:
    count = 0
    def readBinaryWatch(self, num: int) -> List[str]:
        if num == 0:
            return ["0:00"]
        visited = set()
        all_elements = {("hour", 1), ("hour", 2), ("hour", 4), ("hour", 8),
                     ("minutes", 1), ("minutes", 2), ("minutes", 4), ("minutes", 8),
                     ("minutes", 16), ("minutes", 16), ("minutes", 32)}
        result = []
        self.backtrack(visited, all_elements, result, num)
        return result

    def backtrack(self, visited, all_elements, result, num):
        if len(visited) == num:
            self.count += 1
            self.convertResult(visited, result)  # add convert visited to result
            return

        for elem in all_elements:  # take an element from unvisited
            if elem not in visited:
                visited.add(elem)
                self.backtrack(visited, all_elements, result, num)
                visited.remove(elem)

    def convertResult(self, visited, result):
        hours = minutes = 0
        for elem in visited:
            if elem[0] == "hour":
                hours += elem[1]
            else:
                minutes += elem[1]
        if hours <= 11 and minutes <= 59:  # check and validate
            visited_result = "{:d}:{:02d}".format(hours, minutes)
            if visited_result not in result:
                result.append(visited_result)  # add to result


if __name__ == '__main__':
    test = Solution()
    myresult = test.readBinaryWatch(2)
    print(test.count)
    print(len(myresult))
    print(sorted(myresult))
