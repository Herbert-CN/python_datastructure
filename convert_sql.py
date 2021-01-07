class Solution:
    def convertSQL(self, rawString: str) -> str:
        rawList = rawString.split()
        result = []
        counting_start = False
        for element in rawList:
            if element == 'or' and not counting_start:
                temp = result.pop()
                result.append('(')
                result.append(temp)
                counting_start = True
            elif element == 'and' and counting_start:
                result.append(')')
                counting_start = False
            result.append(element)

        if counting_start:
            result.append(')')

        return ' '.join(result)

if __name__ == '__main__':
    test = Solution()

    assert test.convertSQL("a or b") == "( a or b )"

    assert test.convertSQL("a and b or c") == "a and ( b or c )"
    assert test.convertSQL("a and b or c or d") == "a and ( b or c or d )"

    assert test.convertSQL("a and b or c and d or e and f") == "a and ( b or c ) and ( d or e ) and f"