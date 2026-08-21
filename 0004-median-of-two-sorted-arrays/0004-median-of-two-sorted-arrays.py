class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr=sorted(nums1+nums2)
        sums=sum(arr)
        
        if len(arr)%2==1:
            return arr[len(arr)//2]
        else:
            first=len(arr)//2-1
            sec=(len(arr)//2)

            return (arr[first]+arr[sec])/2


        
        