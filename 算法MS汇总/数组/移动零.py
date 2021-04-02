'''
283.移动零
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
示例:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:
必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。

考查标签 数组、指针
'''


# 快慢指针
class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slowindex = 0
        for fastindex in range(len(nums)):
            if nums[fastindex] != 0:
                nums[slowindex] = nums[fastindex]
                slowindex += 1
        # 将slowindex之后的冗余元素赋值为0
        for j in range(slowindex, len(nums)):
            nums[j] = 0
        print(nums)


a = Solution()
a.moveZeroes([0, 1])

'''
代码讲解网址：
https://leetcode-cn.com/problems/move-zeroes/solution/283-yi-dong-ling-shuang-zhi-zhen-xiang-jie-by-ca-2/
'''