#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.Stack=[]
        self.length=0
    def addNum(self, num: int) -> None:
        ### using binary search to insert element
        index=self.binarySearch(num)
        self.Stack.insert(index,num)
        self.length+=1
    def findMedian(self) -> float:
        if self.length%2==0:
            return (self.Stack[self.length//2]+self.Stack[self.length//2-1])/2.0
        else:
            return self.Stack[self.length//2]
    def binarySearch(self,num:int)->int:
        start,end=0,self.length-1
        while start<=end:
            mid=start+(end-start)//2
            if self.Stack[mid]<num:
                start=mid+1
            else:
                end=mid-1
        return start


        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(1)
# obj.addNum(2)
# obj.addNum(8)
# obj.addNum(6)
# print(obj.length)
# param_2 = obj.findMedian()
# print(param_2)
