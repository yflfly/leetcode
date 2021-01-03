'''
面试题 10.02. 变位词组
编写一种方法，对字符串数组进行排序，将所有变位词组合在一起。变位词是指字母相同，但排列不同的字符串。
注意：本题相对原题稍作修改
示例:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
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
        res = {}
        for each in strs:
            sort_str = ''.join(sorted(each))
            res[sort_str] = res.get(sort_str, []) + [each]
        return [vals for vals in res.values()]


'''
遍历数组，把每个字符串排序后的值作为key保存到字典中，在对应的value中添加原字符串。
'''
