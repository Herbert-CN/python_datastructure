"""
Design the CombinationIterator class:

CombinationIterator(string characters, int combinationLength) Initializes the object with a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
next() Returns the next combination of length combinationLength in lexicographical order.
hasNext() Returns true if and only if there exists a next combination.


Example 1:

Input
["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[["abc", 2], [], [], [], [], [], []]
Output
[null, "ab", true, "ac", true, "bc", false]

Explanation
CombinationIterator itr = new CombinationIterator("abc", 2);
itr.next();    // return "ab"
itr.hasNext(); // return True
itr.next();    // return "ac"
itr.hasNext(); // return True
itr.next();    // return "bc"
itr.hasNext(); // return False


Constraints:

1 <= combinationLength <= characters.length <= 15
All the characters of characters are unique.
At most 104 calls will be made to next and hasNext.
It's guaranteed that all calls of the function next are valid.
"""


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self._chars = sorted([ch.lower() for ch in characters])
        self._length = combinationLength
        self._result = []
        self._dfs(self._chars, self._length, [], self._result)

    def next(self) -> str:
        return self._result.pop(0)

    def hasNext(self) -> bool:
        return True if self._result else False

    def _dfs(self, chars, length, path, result):
        if len(path) == length:
            result.append("".join(path))
            return

        for i in range(len(chars)):
            self._dfs(chars[i+1:], length, path+[chars[i]], result)

if __name__ == '__main__':
    obj = CombinationIterator("abc", 2)
    print(obj.next())
    print(obj.hasNext())
    print(obj.next())
    print(obj.hasNext())
    print(obj.next())
    print(obj.hasNext())


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()