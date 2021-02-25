'''
删除排序数组中的重复项
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
示例 1:
给定数组 nums = [1,1,2],
函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
你不需要考虑数组中超出新长度后面的元素。
示例 2:
给定 nums = [0,0,1,1,1,2,2,3,3,4],
函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
你不需要考虑数组中超出新长度后面的元素。

考查标签：数组、双指针
'''

# 方法：双指针

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[slow] == nums[fast]:
                fast += 1
            else:
                nums[slow+1] = nums[fast]
                slow += 1
                fast += 1
        return slow+1

'''
数组完成排序后，可以放置两个指针slow、fast
若nums[slow] == nums[fast]，则增加fast以跳过重复项
若nums[slow] != nums[fast]，跳过重复项的运行已经结束，因此nums[slow+1] = nums[fast]，然后递增slow、fast
接着我们将再次重复相同的过程，直到fast到达数组的末尾为止
'''