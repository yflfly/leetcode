# coding:utf-8
'''
40. 组合总和 II
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。
说明：
所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:
输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:
输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
'''


# 超出时间限制
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        if not candidates:
            return []
        candidates.sort()
        n = len(candidates)

        def trace_back(i, temp, target):
            if target == 0 and temp not in res:
                res.append(temp)
                return
            if i == n or target < candidates[i]:
                return
            for j in range(i, n):
                trace_back(j + 1, temp + [candidates[j]], target - candidates[j])

        trace_back(0, [], target)
        return res


'''
因为是要给出每一种不重复的解集，因此肯定是要对每一种情况都尝试一遍，就容易想到是使用回溯的算法思路来解决这道题。

①首先需要对candidates集合进行升序排列。这是因为排列之后，如果遇到某个集合里面的元素candidates[i]大于我们的目标值target,那么直接结束本次尝试，进行下一次回溯。便于处理，减少回溯次数。

②在回溯的过程中，建立一个临时的list集合temp，将当前处理的元素candidates[i]先加入temp中，加进去之后，target - candidates[i]；结束回溯的条件就是target = 0，当temp满足和为target的时候，代表他是一个解，因此加入res集合中。起到累加计算和的过程。

③在这道题中还有一个限制条件，就是不能有重复的解，因此要对回溯进行“剪枝”操作，因此在加入res集合之前，判断这个解是否已经在res中了，因此：temp not in res 时，作为一个解加入res。在第一次的代码中没有注意这一点，就出现了重复的解。
'''


class Solution(object):
    def combinationSum2(self, candidates, target):
        def dfs(candidates, path, begin, ans, res):
            # candidates：题目中的数组
            # path：用来保存每次的路径path，符合条件则加入结果数组res
            # begin：用来表示当前循环for所到达的位置（即i），然后下一层回溯就可以从下一个值i+1开始，防止重复前面元素
            # ans：用来保存路径上经历过的元素的和，用来与target比较
            # res：用来保存结果数组

            if ans > target:  # 不符合，返回上一层找其他路径
                return
            if ans == target:  #  符合条件，加入数组
                res.append(path[:])
                return

            for i in range(begin, n):
                if i > begin and candidates[i - 1] == candidates[i]:  # 如果有重复的值，跳过
                    continue

                # 每次path加入candidates[i]的值，begin为i+1，ans就加上candidates的值
                dfs(candidates, path + [candidates[i]], i + 1, ans + candidates[i], res)

        n = len(candidates)
        res = []

        candidates.sort()  # 不要忘记先对candidates排序
        dfs(candidates, [], 0, 0, res)
        return res


'''
全局变量：res = []
参数设计：（1）状态变量：当前选用过的数字（2）条件变量：剩余的备选数字 和 当前数字的总和。
完成条件：当数字总和等于target了，就加入到res；当大于target了，则不再搜索；当小于target了，就继续搜索。
递归过程：如果当前总和小于target就继续搜索。
'''


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        state = []
        s = set()

        def back(state, p, count):
            for i in range(p, len(candidates)):
                temp_count = count + candidates[i]
                temp_state = state + [candidates[i]]
                if temp_count < target:
                    back(temp_state, i + 1, temp_count)
                else:
                    if temp_count == target and tuple(temp_state) not in s:
                        s.add(tuple(temp_state))
                        res.append(temp_state)
                    return

        candidates.sort()
        back(state, 0, 0)
        return res
