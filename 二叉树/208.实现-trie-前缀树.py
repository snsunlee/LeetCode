#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#
class Trie:
###{a:{p:{p:{'666':1,l:{e:{'666':1}}}}}}
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_map={}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        dict_insert=self.hash_map
        for char in word:
            if char in dict_insert:
                dict_insert=dict_insert[char]
            else:
                dict_insert[char]={}
                dict_insert=dict_insert[char]
        dict_insert['666']=1



    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        dict_search=self.hash_map
        for char in word:
            if char in dict_search:
                dict_search=dict_search[char]
            else:
                return False
        if '666' in dict_search:
            return True
        return False
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        dict_check=self.hash_map
        for char in prefix:
            if char in dict_check:
                dict_check=dict_check[char]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

