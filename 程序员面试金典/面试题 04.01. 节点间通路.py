'''
面试题 04.01. 节点间通路
节点间通路。给定有向图，设计一个算法，找出两个节点之间是否存在一条路径。
示例1:
 输入：n = 3, graph = [[0, 1], [0, 2], [1, 2], [1, 2]], start = 0, target = 2
 输出：true
示例2:
 输入：n = 5, graph = [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3], [3, 4]], start = 0, target = 4
 输出 true
'''


class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        # 构建邻接表
        link_table = [[] for _ in range(n)]
        for i, j in graph:
            link_table[i].append(j)
        visted = [0] * n  # 访问数组
        # BFS
        que = [start]
        while que:
            cur_node = que.pop()
            if target in link_table[cur_node]:
                return True
            for node in link_table[cur_node]:
                if visted[node] == 0:
                    que.insert(0, node)
            visted[cur_node] = 1
        return False


'''
解题思路
构建邻接表，将每个结点的邻接结点表示出来，便于后续遍历
利用队列进行BFS，访问当前结点邻接结点，未访问过得结点加进队列，直至队列为空
访问完当前结点的所有邻接结点，将该点visted置为1

判定条件
能访问到目标结点——True
1- visted[target]==1
2- target in link_table[cur_node]
遍历结束也没找到——False
'''
