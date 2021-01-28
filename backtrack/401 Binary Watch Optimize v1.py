"""
Version 1
"""

from typing import List


class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        if num == 0:
            return ["0:00"]
        visited = set()
        all_elements = {("hour", 1), ("hour", 2), ("hour", 4), ("hour", 8),
                        ("minute", 1), ("minute", 2), ("minute", 4), ("minute", 8),
                        ("minute", 16), ("minute", 16), ("minute", 32)}
        result = set()
        self.backtrack(visited, all_elements, result, num)
        return list(result)

    def backtrack(self, visited, all_elements, result, num, curHour=0, curMinutes=0):
        if len(visited) == num:
            if "{:d}:{:02d}".format(curHour, curMinutes) not in result:
                result.add("{:d}:{:02d}".format(curHour, curMinutes))
            return

        for elem in all_elements:  # take an element from unvisited
            if elem not in visited:
                if elem[0] == "hour" and curHour + elem[1] <= 11:
                    visited.add(elem)  # 加入的时候进行优化
                    self.backtrack(visited, all_elements, result, num, curHour + elem[1], curMinutes)
                    visited.remove(elem)
                elif elem[0] == "minute" and curMinutes + elem[1] <= 59:
                    visited.add(elem)  # 加入的时候进行优化
                    self.backtrack(visited, all_elements, result, num, curHour, curMinutes + elem[1])
                    visited.remove(elem)
                else:
                    continue

if __name__ == '__main__':
    test = Solution()
    myresult = test.readBinaryWatch(3)

    print(len(myresult))
    print(sorted(myresult))
