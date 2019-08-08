#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        import re
        res = re.findall(r"^[\+\-]?\d+",str.strip())
        print(res)
        if res !=[]:
            if int(res[0]) > (2**31-1):
                return (2**31-1)
            if int(res[0]) < (-2**31):
                return (-2**31)
            return int(res[0])
        else:
            return 0

