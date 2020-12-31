'''
面试题 16.11. 跳水板
你正在使用一堆木板建造跳水板。有两种类型的木板，其中长度较短的木板长度为shorter，长度较长的木板长度为longer。你必须正好使用k块木板。编写一个方法，生成跳水板所有可能的长度。
返回的长度需要从小到大排列。
示例 1
输入：
shorter = 1
longer = 2
k = 3
输出： [3,4,5,6]
解释：
可以使用 3 次 shorter，得到结果 3；使用 2 次 shorter 和 1 次 longer，得到结果 4 。以此类推，得到最终结果。
'''
'''
1.解题思路
主要考虑 longer > shorter 的情况，板长的范围一定在 [shorter * k, longer * k]闭区间，在严格大于的情况下，每用一块长的代替一块短的，必然增加 longer-shorter 的长度。那么从最短的 shorter*k ,即用 k 个短板，每替换其中的一个板为长板，就会在上一步上加 longer - shorter , 了解到这里，代码就很容易想了。
'''
class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k == 0: # 如果k为0，代表没有木板，返回空
             return []
        if shorter == longer:  # 若长板和短板一样长，那么长度只有一种
            return [shorter * k]
        # 下面情况发生在 longer 严格大于 shorter 的情况下
        res = []
        start = shorter * k
        diff = longer - shorter  #
        for i in range(k + 1):
            res.append(diff * i + start)
        return res
