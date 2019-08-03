#
# @lc app=leetcode.cn id=779 lang=python3
#
# [779] 第K个语法符号
#
# https://leetcode-cn.com/problems/k-th-symbol-in-grammar/description/
#
# algorithms
# Medium (37.90%)
# Likes:    32
# Dislikes: 0
# Total Accepted:    1.8K
# Total Submissions: 4.6K
# Testcase Example:  '1\n1'
#
# 在第一行我们写上一个 0。接下来的每一行，将前一行中的0替换为01，1替换为10。
# 
# 给定行数 N 和序数 K，返回第 N 行中第 K个字符。（K从1开始）
# 
# 
# 例子:
# 
# 输入: N = 1, K = 1
# 输出: 0
# 
# 输入: N = 2, K = 1
# 输出: 0
# 
# 输入: N = 2, K = 2
# 输出: 1
# 
# 输入: N = 4, K = 5
# 输出: 1
# 
# 解释:
# 第一行: 0
# 第二行: 01
# 第三行: 0110
# 第四行: 01101001
# 
# 
# 
# 注意：
# 
# 
# N 的范围 [1, 30].
# K 的范围 [1, 2^(N-1)].
# 
# 
#
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if(N==1 and K==1):
            return 0
        a=self.kthGrammar(N-1,(K+1)//2)  #求父结点的值；(K+1)/2为父结点的序号
        b=-(a-1)                         #a=0则b=1,若a=1则b=0
        if(K%2==1):
            return a                     #K为奇数则其值与父结点相同
        else:
            return b

# //序号
# //              1(0)
# //          /        \   
# //     1(0)            2(1)
# //    /   \            /    \
# // 1(0)    2(1)     3(1)   4(0)
# // / \     /  \     /  \    / \ 
# //1(0)   2   3    4   5    6  7   8

# //01排列
# //              0
# //          /        \   
# //      0                1
# //    /   \            /    \
# //  0       1        1       0
# // / \     /  \     /  \    / \ 
# //0   1   1    0   1    0  0   1 
###超时做法：
    # def kthGrammar(self, N: int, K: int) -> int:
    #     if N==1:
    #         return '0'
    #     base={'0':'01','1':'10'}
    #     def helper(column,string):
    #         newString=''.join(list(map(lambda x:base[x],list(string))))
    #         if column==N-1:
    #             return newString
    #         return helper(column+1,newString)
        
    #     newString=helper(1,'0')
    #     return newString[K-1]
