# coding:utf-8
'''
堆排序
构造堆：从小堆到大堆，先看最后一个非叶子节点，从下往上
时间复杂度 ： o(nlogn)
'''


# 向下调整函数的实现, 此处建立大根堆，可实现数组升序排列
def sift(alist, low, high):
    # 假设只有根节点需要调整，两棵子树都是堆
    i = low
    j = i * 2 + 1  # j指向i的左子树
    tmp = alist[i]
    while j <= high:
        if j + 1 <= high and alist[j] < alist[j + 1]:  # 右子树比较大,则指向右子树
            j = j + 1
        if alist[j] > tmp:  # 若子树的值比较大，则根节点换成子树，然后向下看一层
            alist[i] = alist[j]
            i = j
            j = i * 2 + 1
        else:
            alist[i] = tmp  # 子树的值小于根节点，则根节点就放在这一层
            break
    else:
        alist[i] = tmp  # j越界跳出循环，则把根节点放在叶子节点


def heap_sort(alist):
    # 1、建堆
    # 先找到最后一个不是叶子节点的根节点，为(n-2)//2 (若叶子节点为i，则他的父节点为(i-1)//2 )
    # 再向上循环根节点，从小到大
    n = len(alist)
    for i in range((n - 2) // 2, -1, -1):
        sift(alist, i, n - 1)
    print('创建堆之后的结果', alist) # [93, 77, 54, 55, 26, 31, 44, 17, 20, 13]

    # 2、挨个出数，按升序排列
    for i in range(n - 1, -1, -1):
        alist[0], alist[i] = alist[i], alist[0]
        sift(alist, 0, i - 1)


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20, 13]
    heap_sort(li)
    print(li)  # [13, 17, 20, 26, 31, 44, 54, 55, 77, 93]

'''
堆一般指的是二叉堆，顾名思义，二叉堆是完全二叉树或者近似完全二叉树
堆的性质：
1）是一棵完全二叉树
2）每个节点的值都大于或等于其子节点的值，为最大堆，反之为最小堆
堆的存储：一般用数组来表示堆，下标为 i 的结点的父结点下标为(i-1)/2；其左右子结点分别为 (2i + 1)、(2i + 2)

堆的操作：
在堆的数据结构中，堆中的最大值总是位于根节点(在优先队列中使用堆的话堆中的最小值位于根节点)。堆中定义以下几种操作：
1）最大堆调整（Max_Heapify）：将堆的末端子节点作调整，使得子节点永远小于父节点
2）创建最大堆（Build_Max_Heap）：将堆所有数据重新排序
3）堆排序（HeapSort）：移除位在第一个数据的根节点，并做最大堆调整的递归运算

实现堆排序需要解决两个问题：
1）如何由一个无序序列建成一个堆？
2）如何在输出堆顶元素之后，调整剩余元素成为一个新的堆？
'''
