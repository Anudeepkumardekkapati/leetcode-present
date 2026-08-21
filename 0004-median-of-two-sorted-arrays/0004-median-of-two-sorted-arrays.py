class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return self.merge(nums1,nums2)
    def merge(self,nums1,nums2):
        i=0
        j=0
        res=[]
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                res.append(nums1[i])
                i+=1
            else:
                res.append(nums2[j])
                j+=1
        res.extend(nums1[i:])
        res.extend(nums2[j:])
        if len(res)%2==1:
            return res[len(res)//2]
        else:
            first=(len(res)//2)-1
            sec=len(res)//2
            return (res[first]+res[sec])/2

        
            



        
        