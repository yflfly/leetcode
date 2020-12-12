# coding:utf-8
'''
面试题 17.08. 马戏团人塔
有个马戏团正在设计叠罗汉的表演节目，一个人要站在另一人的肩膀上。
出于实际和美观的考虑，在上面的人要比下面的人矮一点且轻一点。
已知马戏团每个人的身高和体重，请编写代码计算叠罗汉最多能叠几个人。
示例：
输入：height = [65,70,56,75,60,68] weight = [100,150,90,190,95,110]
输出：6
解释：从上往下数，叠罗汉最多能叠 6 层：(56,90), (60,95), (65,100), (68,110), (70,150), (75,190)
提示：
height.length == weight.length <= 10000
'''


class Solution:
    def bestSeqAtIndex(self, height: List[int], weight: List[int]) -> int:
        hw = sorted(zip(height, weight))

        dp = []  # dp[i]: 长度为(i+1)的(height, weight)双严格上升子序列中，末尾的weight最小是多少
        temp = []
        for i in range(len(hw)):
            # temp: 记录(要填入的体重, 要填入的位置)
            temp.append((hw[i][1], bisect.bisect_left(dp, hw[i][1])))

            # 到达尽头或下一个height严格变大时，开始填入
            if i == len(hw) - 1 or hw[i][0] < hw[i + 1][0]:
                for w, i in temp:
                    # 添加到dp末尾
                    if i == len(dp):
                        dp.append(w)
                    # 更新dp[i]；注意同一height下weight是递增的，所以不能直接赋值，要取较小者
                    else:
                        dp[i] = min(dp[i], w)
                temp = []
        return len(dp)
