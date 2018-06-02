# _*_ coding: utf-8 _*_
__author__ = 'daiyaquan'
__date__ = '2018/6/2 18:01'


class Solution:
    def levelOrder(self, root):
        """
        1. 队列存节点, 层数
        2. 初始化存根节点
        3. 不断的出队, 将值保存在结果集相应的位置, 将左右节点在加入队列, 注意层数
        4. 如果当期层数没出现过, 并且对应节点非空则增加一个该层对应的list
        """
        # 步骤1, 2
        from collections import deque
        node_queue = deque()
        node_queue.append((root, 0))

        res, res_set = [], set()

        # 步骤3
        while node_queue:
            node, level = node_queue.popleft()
            # 步骤四
            if node:
                if level not in res_set:
                    res_set.add(level)
                    res.append([])
                res[level].append(node.val)
                node_queue.append((node.left, level + 1))
                node_queue.append((node.right, level + 1))

        return res
