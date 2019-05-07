# LeetCode 11.盛最多水的容器
## 题目描述
给定 $n$个非负整数 $a_1,a_2,a_3...，a_n$每个数代表坐标中的一个点 $(i, a_i)$ 。在坐标内画 $n$ 条垂直线，垂直线$i$的两个端点分别为$(i, a_i)$和$(i, 0)$。找出其中的两条线，使得它们与$x$轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器，且$n$的值至少为 2。
![img](https://aliyun-lc-upload.oss-cn-hangzhou.aliyuncs.com/aliyun-lc-upload/uploads/2018/07/25/question_11.jpg)

### 示例：
```
输入: [1,8,6,2,5,4,8,3,7]
输出: 49 
```

### 解题思路
最开始我是用两遍循环暴力来做，这个就按下不表了。其实题目的目的是想最大化这个矩形的面积，俗话说：木桶能装多少水要看最短的那根木板有多短。
设置首尾双指针$i$和$j$，依次计算面积，每次移动短的一端的指针，不断去逼近最大值。而为什么要舍弃较短的木板呢？
假设第一根比最后一根短，此时计算的面积一定大于等于任何一个以第一根为边的板子所计算的面积，也就是说我们在任意再从所有板中选2个，保证一个选第一根的情况下 （比如说我们选1和n-1 两条板子)，它的面积一定小于等于我们头尾的面积。

### Python代码
``` Python
class Solution:
    def maxArea(self, height) -> int:
        left,right=0,len(height)-1
        maxVal=0
        while left<right:
            maxVal=max(maxVal,min(height[left],height[right])*(right-left) )
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxVal
```

