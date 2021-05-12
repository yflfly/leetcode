'''
面试题 17.05.  字母与数字
给定一个放有字符和数字的数组，找到最长的子数组，且包含的字符和数字的个数相同。
返回该子数组，若存在多个最长子数组，返回左端点下标值最小的子数组。若不存在这样的数组，返回一个空数组。
示例 1:
输入: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"]
输出: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7"]
示例 2:
输入: ["A","A"]
输出: []
'''


# 前缀和系列
class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        dic = {0: 0}
        count = 0
        ans_idx, ans_val = (0, 0), 0
        for i in range(len(array)):
            if array[i].isnumeric():
                count += 1  # 统计数字和字母的差 差值字典
            else:
                count -= 1
            if count in dic:
                l, r = dic[count], i + 1
                if r - l + 1 > ans_val:
                    ans_idx, ans_val = (l, r), r - l + 1
            else:
                dic[count] = i + 1
        return array[ans_idx[0]:ans_idx[1]]
