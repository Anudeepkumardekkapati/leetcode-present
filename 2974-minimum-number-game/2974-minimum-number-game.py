import heapq
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr=[]
        while len(nums)!=0:
            alice=heapq.heappop(nums)
            bob=heapq.heappop(nums)
            arr.append(bob)
            arr.append(alice)
        return arr
        

        