# coding:utf-8
'''
面试题 10.03. 搜索旋转数组
搜索旋转数组。给定一个排序后的数组，包含n个整数，但这个数组已被旋转过很多次了，次数不详。请编写代码找出数组中的某个元素，假设数组元素原先是按升序排列的。若有多个相同元素，返回索引值最小的一个。
示例1:
 输入: arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target = 5
 输出: 8（元素5在该数组中的索引）
示例2:
 输入：arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target = 11
 输出：-1 （没有找到）
'''
# 方法一
class Solution:
    def search(self, arr: List[int], target: int) -> int:
        if target in arr:
            return arr.index(target)
        else:
            return -1
# 方法二
'''
此题相比于无重复元素的普通旋转数组搜索问题来说，增加了两个点：
1.多次旋转而不是一次旋转，但其实多次旋转与一次旋转效果是相同的，因此可以忽略这一变化；
2.有重复元素，这是比较难的一个点；

在二分查找之前，我们判断是否存在数组首尾元素相同且为目标数的情况，例如[2,2,2,1,2] 2,[5,5,5,1,2,3,4,5] 5这些情况，则可以直接返回首索引，算法结束，这样就排除了目标数落在无序区间的情况。

然后我们开始二分查找，每次寻找有序区间并判断目标数是否在其中，从而确定下一步的查找区间。当出现arr[low] == arr[mid]的特殊情况时，若arr[low]为目标数，直接返回索引low即可，否则low进行自加，对重复元素逐个排除。

二分查找结束后，再判断索引low对应元素是否为目标数即可。

'''
class Solution:
    def search(self, arr: List[int], target: int) -> int:
        n = len(arr)
        if n == 0:
            return -1
        low, high = 0, n - 1
        while low < high:
            mid = (low + high) // 2
            if arr[low] == arr[high] == target:
                return low
            if arr[low] < arr[mid]:
                if arr[low] <= target <= arr[mid]:
                    high = mid
                else:
                    low = mid + 1
            elif arr[low] > arr[mid]:
                if arr[mid] < target <= arr[high]:
                    low = mid + 1
                else:
                    high = mid
            else:
                if arr[low] == target:
                    return low
                else:
                    low += 1
        return low if arr[low] == target else -1

