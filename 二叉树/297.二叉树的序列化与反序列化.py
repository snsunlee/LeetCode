#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def __init__(self):
        self.string=""
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def serializeCore(root):
            if not root:
                self.string+="null,"
            else:
                self.string+=str(root.val)+','
                self.serialize(root.left)
                self.serialize(root.right)
        serializeCore(root)
        return self.string
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def deserializeCore(data):
            if data[0]=='null':
                data.pop(0)
                return None
            root=TreeNode(data[0])
            data.pop(0)
            root.left=deserializeCore(data)
            root.right=deserializeCore(data)
            return root
        data=data.split(',')
        root=deserializeCore(data)
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

