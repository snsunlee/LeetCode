#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        def back(i, j, k, visited):
            ##i：index_raw
            ##j:index_column
            ##k:len of visited word
            ##visited: {(index_raw,index_column)}
            #print(i,j, k,visited)
            if k == len(word):###end of visitied
                return True
            for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:###choice of next step
                tmp_i = x + i
                tmp_j = y + j
                if 0 <= tmp_i < row and 0 <= tmp_j < col and (tmp_i, tmp_j) not in visited and board[tmp_i][tmp_j] == word[k]:
                    visited.add((tmp_i, tmp_j))
                    if back(tmp_i, tmp_j, k+1, visited):
                        return True
                    visited.remove((tmp_i, tmp_j)) # 回溯
            return False
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0] and back(i, j, 1,{(i, j)}) :
                        return True
        return False

