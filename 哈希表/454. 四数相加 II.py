'''
454. 四数相加 II
给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。
为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。
例如:
输入:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
输出:
2
解释:
两个元组如下:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
'''


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dicAB = {}
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                tmp = nums1[i]+nums2[j]
                if tmp in dicAB:
                    dicAB[tmp] += 1
                else:
                    dicAB[tmp] = 1
        ans = 0
        for k in range(len(nums3)):
            for l in range(len(nums4)):
                tmp = -nums3[k]-nums4[l]
                if tmp in dicAB:
                    ans += dicAB[tmp]
        return ans
'''
算法思路：
方法：分组 + 哈希表
我们可以将四个数组分成两部分，A和B为一组，C和D为另外一组。
对于A和B，我们使用二重循环对它们进行遍历，得到所有A[i]+B[j]的值并存入哈希映射中。对于哈希映射中的每个键值对，每个键表示一种 A[i]+B[j]，对应的值为A[i]+B[j]出现的次数。
对于C和D，我们同样使用二重循环对它们进行遍历。当遍历到 C[k]+D[l]时，如果-(C[k]+D[l]) 出现在哈希映射中，那么将 -(C[k]+D[l])对应的值累加进答案中。
最终即可得到满足 A[i]+B[j]+C[k]+D[l]=0的四元组数目。

复杂度分析
时间复杂度：O(n^2)。我们使用了两次二重循环，时间复杂度均为O(n^2)。在循环中对哈希映射进行的修改以及查询操作的期望时间复杂度均为 O(1)，因此总时间复杂度为O(n^2)。
空间复杂度：O(n^2)，即为哈希映射需要使用的空间。在最坏的情况下，A[i]+B[j]的值均不相同，因此值的个数为 n^2，也就需要 O(n^2) 的空间。

'''