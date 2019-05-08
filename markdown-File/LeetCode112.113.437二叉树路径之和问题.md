# LeetCode 112.路径之和
## 题目描述
给定一个二叉树和一个目标和，判断该树中是否存在 根节点 到 叶子节点 的路径，这条路径上所有节点值相加等于目标和。
说明: 叶子节点是指没有子节点的节点。

### 示例：
```
给定如下二叉树，以及目标和（sum = 22）
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
```

### 解题思路
一个简单的层次遍历，每次访问节点都将目标和减去当前节点的值变为新的目标和` (sum=sum-root.val)`，继续遍历，当遍历到叶子节点 `(isLeaf=root.left==None and root.right==None) ` 时，只需判断叶子节点的值是否等于目标和 `(sum==root.val)` 即可。递归当然还要注意递归出口。

### Python代码
``` Python
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return True if root.val==sum else False
        return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val) 
```


***

# LeetCode 113.路径之和ii
## 题目描述
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
说明: 叶子节点是指没有子节点的节点。

### 示例：
```
给定如下二叉树，以及 目标和（sum = 22），
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1

返回：
[
   [5,4,11,2],
   [5,8,4,5]
]
```

### 解题思路
这题和上一题相比，是不光要求出存不存在，还需要记录每一条可行的路径，其实在基础的深度优先遍历上就可以写出来。
`dfs()`这个函数传入四个值 ` root节点 target目标和 res满足路径和要求的二维数组 path当前路径的一位数组` 当找到一条可行的路径时 `sum(path)==target and isLeaf `将此时的` path添加到res`
如果当前路径并不满足，则继续遍历，此时需要更新 ` path=path+[root.val]将现在的节点添加到路径中` 

### Python代码
``` Python
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:return[]
        res=[]
        self.dfs(root,sum,res,[root.val])
        return res
    def dfs(self,root,target,res,path):
        if not root:return 
        if sum(path)==target and not root.left and not root.right:###找到一个
            res.append(path)
            return
        if root.left:self.dfs(root.left,target,res,path+[root.left.val])
        if root.right:self.dfs(root.right,target,res,path+[root.right.val])
```
***

# LeetCode 437.路径之和iii
## 题目描述
给定一个二叉树，它的每个结点都存放着一个整数值。
找出路径和等于给定数值的路径总数。
路径 **不需要**从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。
### 示例：
```
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1


返回 3。
和等于 8 的路径有:
1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11
```

### 解题思路
首先满足条件的路径包括 
- 从根节点到某一个节点的
- 非根节点到某一个节点
`findPath()`定义了从根节点到某一节点的满足路径之和的数目
而非根节点无非就是将子节点当做根节点的一种情况，`利用pathSum()依次遍历即可`
### Python代码
``` Python
class Solution:
    def findPath(self, root, sum):###查找包含 root 根节点的 路径之和 的数目
        result = 0
        if not root:
            return result

        if root.val == sum:
            result += 1

        result += self.findPath(root.left, sum - root.val)
        result += self.findPath(root.right, sum - root.val)
        return result
        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        result = 0
        if not root:
            return result

        result += self.findPath(root, sum)
        result += self.pathSum(root.left, sum)
        result += self.pathSum(root.right, sum)
        return result
```

