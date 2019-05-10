#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#
class Solution:
    def convertToTitle(self, n: int) -> str:
        hash_list=' A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
        print(hash_list)
        res=[]
        while n:
            n-=1
            res.insert(0,hash_list[n%26])
            n=n//26
        return ''.join(res)

