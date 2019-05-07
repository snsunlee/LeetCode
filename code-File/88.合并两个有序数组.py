#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for _ in range(len(nums1)-m):
            nums1.pop()
        for i in nums2:
            index=self.binarySearch(nums1,i)
            nums1.insert(index,i)
        
        print(nums1)
    def binarySearch(self,nums,value):
        left=0
        right=len(nums)-1
        
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]==value:
                return mid
            elif nums[mid]<value:
                left=mid+1
            else:
                right=mid-1
        return left
        

