#
# @lc app=leetcode.cn id=380 lang=python3
#
# [380] 常数时间插入、删除和获取随机元素
#
from random import randint

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_index_map = dict()
        self.index_key_map = dict()
        self.index = 0
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.key_index_map:
            self.index += 1
            self.key_index_map[val] = self.index
            self.index_key_map[self.index] = val
            return True
        else:
            return False
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.key_index_map:
            return False
        else:
            remove_index = self.key_index_map[val]
            # 替换 每次都将要删除吧的val 放置在最新的index 从而保证 index_key：1-index是一个连续存储的hash
            self.index_key_map[remove_index] = self.index_key_map[self.index]
            self.key_index_map[self.index_key_map[self.index]] = remove_index
            # 弹出 remove 元素
            self.key_index_map.pop(val)
            self.index_key_map.pop(self.index)
            self.index -= 1
            return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.index_key_map[randint(1, self.index)]
    def getAll(self):
        print("index_key: ",self.index_key_map)
        print("key_index: ",self.key_index_map)
        print("index :",self.index)
# Your RandomizedSet object will be instantiated and called as such:
