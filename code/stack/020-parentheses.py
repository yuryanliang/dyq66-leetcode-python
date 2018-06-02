# _*_ coding: utf-8 _*_
__author__ = 'daiyaquan'
__date__ = '2018/6/2 12:04'


class Solution:
    def isValid(self, s):
        """
        1. 使用栈的原因：需要比较最近的括号
        2. 创建hashmap, key是入栈的，value是出栈的
        3. 遍历字符串
           字符是key：就入栈
           不是：如果栈空 或 出栈的map不等于当前字符 -> False
        4. 遍历完栈中还有就是False
        """
        # 步骤1
        parentheses = {
            '{': '}',
            '[': ']',
            '(': ')'
        }

        # 步骤2
        stack = []

        for item in s:
            if item in parentheses:
                stack.append(item)
            else:
                if not stack or parentheses[stack.pop()] != item:
                    return False

        # 步骤3
        if stack:
            return False

        return True
