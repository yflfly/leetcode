# coding:utf-8

# 斐波那契递归测试
def fibonacciRecursive(deepth):
    if deepth == 1:
        return 1
    elif deepth == 2:
        return 1
    else:
        return fibonacciRecursive(deepth - 1) + fibonacciRecursive(deepth - 2)


# 斐波那契尾递归测试
def fibonacciTailRecursive(num, ret1, rte2):
    if num == 1:
        return rte2
    return fibonacciTailRecursive(num - 1, rte2, ret1 + rte2)


if __name__ == "__main__":
    a = fibonacciRecursive(30)
    print(a)
    a = fibonacciTailRecursive(30, 0, 1)
    print(a)
