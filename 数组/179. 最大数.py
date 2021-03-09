'''
179. 最大数
给定一组非负整数 nums，重新排列它们每个数字的顺序（每个数字不可拆分）使之组成一个最大的整数。
注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
示例 1：
输入：nums = [10,2]
输出："210"
示例 2：
输入：nums = [3,30,34,5,9]
输出："9534330"
示例 3：
输入：nums = [1]
输出："1"
示例 4：
输入：nums = [10]
输出："10"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution(object):
    def largestNumber(self, nums):
        n = len(nums)

        for i in range(n):
            for j in range(n - i - 1):
                temp_1 = str(nums[j])
                temp_2 = str(nums[j + 1])
                if (int(temp_1 + temp_2) < int(temp_2 + temp_1)):
                    temp = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = temp
        output = ''
        for num in nums:
            output = output + str(num)
        return str(int(output))


'''
这是一个需要考虑 "权重" 的问题，此处的权重就是两个元素a和b的排序带来的不同，a+b和b+a的大小判断。
'''
# 防止出现 ‘00’的情况，这样可以把这种情况排除掉

nums = [3, 30, 34, 5, 9]
n = len(nums)
for i in range(n):
    for j in range(n - i - 1):
        print(n, i, j)
        tmp_1 = str(nums[j])
        tmp_2 = str(nums[j + 1])
        if int(tmp_1 + tmp_2) < int(tmp_2 + tmp_1):
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
        print(nums)
    output = ''
    for num in nums:
        output = output + str(num)
    output = str(int(output))
