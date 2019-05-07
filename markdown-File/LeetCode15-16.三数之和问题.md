# LeetCode 15.三数之和
## 题目描述
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。

### 示例：
```
例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```

### 解题思路
第一种思路就是遍历去找一个和为0的三个元素，除了超时还有一个问题，就是得到的数组 ` [[-1,2,-1],[2,-1,1],[1,0,-1]]`重复的如何去掉，这个还没想到好的方法解决，解决了再update下
思路和下一题比较类似，都是设置首尾两个指针去不断移动，但这一题是去逼近和为0。
首先将数组排序，第一个数字从0（$i$）开始遍历，第二个数字则是从第一个数字的下一位（$j=i+1$）开始，第三个数字则是从（$len(nums)-1$）从后往前开始。
三数和比0大说明，整体大了，第三个数字（$k$）要前移，整体小了，第二个数字（$j$）要后移。
为了避免重复，在 $i,j,k$ 前后移动的时候，发现移动位置后数字没有发生变化时$ （例如：nums[i]==nums[i-1]/nums[k]==nums[k-1]/nums[j]==nums[j+1]）$，需要继续移动，这样可以减小时间复杂度，避免重复。

### Python代码
``` Python
class Solution:
    def threeSum(self, nums):
        result = []
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            while j<k:
                temp = nums[i]+nums[j]+nums[k]
                if temp>0:
                    k = k-1
                elif temp<0:
                    j = j+1
                else:
                    result.append([nums[i],nums[j],nums[k]])
                    ###以下代码用来优化 时间复杂度 去重重复的项目
                    while j<k and nums[j]==nums[j+1]:
                        j = j+1
                    while j<k and nums[k]==nums[k-1]:
                        k = k-1     
                    j = j+1
                    k = k-1
        return result
```




# LeetCode 16.最接近的三数之和
## 题目描述
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

### 示例：
```
例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
```

### 解题思路
最暴力肯定是用三层遍历来做,每次得到一个三数之和与$target$进行比较,记录最小差值时的三数之和，最后输出。$O(n^3)$顶不太住!

首先将数组排序，假设固定第一个数的位置（$i$），来取后面的两个数，他们可以取$[(i+1),len(nums)-1]$，此时用 $j,k$ 来固定后两个数，第二个数的位置（$j$）可以从 $i+1$ 开始取，而第三个数的位置（$k$）可以从 $len(nums)-1$ 开始取，计算 $ nums[i]+nums[j]+nums[k] $ 的值，并与 $target$ 进行比较：

$$
\begin{cases}
j++& \text{nums[i]+nums[j]+nums[k]<target}\\
k--& \text{nums[i]+nums[j]+nums[k]>target}
\end{cases}
$$

### Python代码
``` Python
class Solution:
    def threeSumClosest(self, nums, target):
        result = nums[0]+nums[1]+nums[2]
        dis = abs(result-target)
        nums.sort()
        for i in range(len(nums)):
            num = nums[i]
            j = i+1
            k = len(nums)-1
            while j<k:
                temp = abs(nums[i]+nums[j]+nums[k]-target)
                if temp<dis:
                    dis = temp
                    result = nums[i]+nums[j]+nums[k]
                if nums[i]+nums[j]+nums[k]<target:
                    j += 1
                elif nums[i]+nums[j]+nums[k]>target:
                    k -= 1
                else:
                    return nums[i]+nums[j]+nums[k]
        return result 
```

