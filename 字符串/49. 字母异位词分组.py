'''
49. 字母异位词分组
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
示例:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：
所有输入均为小写字母。
不考虑答案输出的顺序。
'''


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for each in strs:
            str_sort = ''.join(sorted(list(each)))
            if str_sort in dic:
                dic[str_sort].append(each)
            else:
                dic[str_sort] = [each]
        res = []
        for key in dic:
            res.append(dic[key])
        return res
