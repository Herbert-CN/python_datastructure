def function1(n: int):
    if n <= 1:
        return 1
    else:
        return n * function1(n-1)

def function2(n: int):
    if n <= 1:
        return 1
    else:
        n * function2(n-1)


def function4(n: int, result):
    if n <= 1:
        if 1 not in result:
            result.append(1)
        return 1
    else:
        a = n * function4(n-1, result)
        result.append(a)
        return a

if __name__ == '__main__':
    mytest1 = function1(10)
    print(mytest1)

    mytest2 = function2(1)
    print(mytest2)

    # mytest3 = function2(3)
    # print(mytest3)

    result = []
    mytest4 = function4(4, result)
    print(result)
