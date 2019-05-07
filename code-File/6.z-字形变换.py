#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#
import math
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s)<1:
            return s
        s_matrix=[]
        isEven=False
        list_s=list(s)
        while list_s:#列遍历
            if not isEven:#非偶数列
                count_row=0
                if len(list_s)<numRows:
                    s_matrix.append(list_s[:numRows]+(numRows-len(list_s))*[''])
                    list_s=list_s[numRows:]
                    isEven=True
                else:
                    s_matrix.append(list_s[:numRows])
                    list_s=list_s[numRows:]
                    isEven=True
            else:
                if count_row==numRows-2:
                    isEven=False
                    continue
                new_item=['']*(numRows-count_row-2)+list_s[:1]+['']*(count_row+1)
                s_matrix.append(new_item)
                list_s=list_s[1:]
                count_row+=1
        out_s=''
        print(1)
        tran_mat=list(map(list,zip(*s_matrix)))
        for i in range(len(tran_mat)):
            out_s+=''.join(tran_mat[i])
        return out_s

