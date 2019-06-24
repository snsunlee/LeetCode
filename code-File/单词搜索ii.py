"""
给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
示例:
输入: 
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
输出: ["eat","oath"]

说明:
你可以假设所有输入都由小写字母 a-z 组成。
提示:
你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？
如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。什么样的数据结构可以有效地执行这样的操作？散列表是否可行？为什么？ 前缀树如何？如果你想学习如何实现一个基本的前缀树，请先查看这个问题： 实现Trie（前缀树）。
"""
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['#'] = True

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        node = Trie()
        for word in words:
            node.insert(word)
        node = node.root

        visited = [[0] * len(board[0]) for i in range(len(board))]
        result = []
        temp = ''
        row = len(board)
        col = len(board[0])
        for i in range(row):
            for j in range(col):
                if board[i][j] in node:
                    self.dfs(board, i, j, visited, node, temp, result)
        return result
    def dfs(self, board, i, j, visited, node, temp, result):
        row = len(board)
        col = len(board[0])

        if '#' in node and temp not in result:
            return result.append(temp)
        if i > row-1 or i < 0 or j > col-1 or j < 0:
            return
        if board[i][j] not in node or visited[i][j] == 1:
            return

        temp += board[i][j]
        visited[i][j] = 1
        self.dfs(board, i + 1, j, visited, node[board[i][j]], temp, result)
        self.dfs(board, i - 1, j, visited, node[board[i][j]], temp, result)
        self.dfs(board, i, j + 1, visited, node[board[i][j]], temp, result)
        self.dfs(board, i, j - 1, visited, node[board[i][j]], temp, result)        
        visited[i][j] = 0


###val:
print(Solution().findWords([
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
],["oath","pea","eat","rain"]))