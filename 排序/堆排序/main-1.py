# coding:utf-8
def heap_sort(elems):
    def siftdown(elems, e, begin, end):  # 向下筛选
        i, j = begin, begin * 2 + 1  # j为i的左子结点
        while j < end:
            if j + 1 < end and elems[j] > elems[j + 1]:  # 如果左子结点大于右子结点
                j += 1  # 则将j指向右子结点
            if e < elems[j]:  # j已经指向两个子结点中较小的位置，
                break  # 如果插入元素e小于j位置的值，则为3者中最小的
            elems[i] = elems[j]  # 能执行到这一步的话，说明j位置元素是三者中最小的，则将其上移到父结点位置
            i, j = j, j * 2 + 1  # 更新i为被上移为父结点的原来的j的位置，更新j为更新后i位置的左子结点
        elems[i] = e  # 如果e已经是某个子树3者中最小的元素，则将其赋给这个子树的父结点
        # 或者位置i已经更新到叶结点位置，则将e赋给这个叶结点。

    end = len(elems)  # 长度为7
    for i in range(end // 2 - 1, -1, -1):  # 构造堆序。i 的取值：2、1、0
        siftdown(elems, elems[i], i, end)
    print('构造的堆', elems)
    for i in range((end - 1), 0, -1):  # 进行堆排序.i最后一个值为1，不需要到0
        # print(elems)
        e = elems[i]  # 将末尾元素赋给e
        elems[i] = elems[0]  # 交换堆顶与最后一个元素
        siftdown(elems, e, 0, i)

    return (elems)


if __name__ == "__main__":
    li = [5, 6, 8, 1, 2, 4, 9]
    li = [50, 16, 30, 10, 60, 90, 2, 80, 70]
    print('初始二叉树', li)
    print(heap_sort(li))

    # li = [50, 16, 30, 10, 60, 90, 2, 80, 70]
'''
上述代码的参考网址：
https://blog.csdn.net/qq_34840129/article/details/80638225
'''