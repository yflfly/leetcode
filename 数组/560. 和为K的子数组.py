# coding:utf-8
'''
560. 和为K的子数组
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
示例 1 :
输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
说明 :
数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
'''


# 下面的方法在提交的过程中会出现超时间限制
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                if sum(nums[i:j]) == k:
                    res.append(nums[i:j])
        return len(res)


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = 0  # 前缀和
        ans = 0
        dp = dict()  # 存放 前缀和:出现次数，键值对，初始化一个0:1，为了考虑到从头开始到某点的子数组正好为答案。
        dp[0] = 1
        for i in range(n):
            pre += nums[i]  # 计算前缀和
            if pre - k in dp:  # 如果pre-k这个前缀存在，那么答案加上它出现的次数
                ans += dp[pre - k]
            if pre in dp:  # 更新dp[pre]
                dp[pre] += 1
            else:
                dp[pre] = 1
        return ans


'''
参考讲解：
https://zhuanlan.zhihu.com/p/135908437
'''
'''
讲解网址：
https://leetcode-cn.com/problems/subarray-sum-equals-k/solution/ha-xi-biao-zhu-xing-jie-shi-python3-by-zhu_shi_fu/
'''


# 方法：哈希表
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash = {0: 1}
        sum = 0
        count = 0
        for i in range(len(nums)):
            sum += nums[i]
            if ((sum - k) in hash):
                count += hash[sum - k]
            if (sum in hash):
                hash[sum] += 1
            else:
                hash[sum] = 1
        return count


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # num_times 存储某“前缀和”出现的次数，这里用collections.defaultdict来定义它
        # 如果某前缀不在此字典中，那么它对应的次数为0
        num_times = collections.defaultdict(int)
        num_times[0] = 1  # 先给定一个初始值，代表前缀和为0的出现了一次
        cur_sum = 0  # 记录到当前位置的前缀和
        res = 0
        for i in range(len(nums)):
            cur_sum += nums[i]  # 计算当前前缀和
            if cur_sum - k in num_times:  # 如果前缀和减去目标值k所得到的值在字典中出现，即当前位置前缀和减去之前某一位的前缀和等于目标值
                res += num_times[cur_sum - k]
            # 下面一句实际上对应两种情况，一种是某cur_sum之前出现过（直接在原来出现的次数上+1即可），
            # 另一种是某cur_sum没出现过（理论上应该设为1，但是因为此处用defaultdict存储，如果cur_sum这个key不存在将返回默认的int，也就是0）
            # 返回0加上1和直接将其置为1是一样的效果。所以这里统一用一句话包含上述两种情况
            num_times[cur_sum] += 1
        return res


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dict1 = {0: 1}  # 表示累加和为0，出现一次
        sums = 0  # 初始累加和为0
        count = 0
        for num in nums:
            sums += num  # 进行累加，即计算前缀和
            if sums - k in dict1:
                '''
                如果当前前缀和减去目标值k之后所得到的值在字典中，转换为当前前缀和减去之前某一位前缀和等于目标值
                即从前面某一位开始到当前位置，这一段连续的子数组的和为k
                '''
                count += dict1[sums - k]
            if sums in dict1:  # 若当前前缀和在字典中，则对应的值加1，否则放进字典中
                dict1[sums] += 1
            else:
                dict1[sums] = 1
        return count
