# _*_ coding: utf-8 _*_
__author__ = 'daiyaquan'
__date__ = '2018/5/30 11:15'


class Solution:
    def isHappy(self, n):
        """
        1. 先余数后地板除来获得一个整数各个数位的值
        2. 如果一个值第二次碰见了，也就是会造成死循环，那么就不是happyNUmber
        """
        seen_set = set()

        while n not in seen_set:
            seen_set.add(n)
            n = sum([i ** 2 for i in self._get_nums(n)])
            if n == 1:
                return True

        return False

    def _get_nums(self, n):
        res = []
        while n:
            res.append(n % 10)
            n //= 10
        return res
