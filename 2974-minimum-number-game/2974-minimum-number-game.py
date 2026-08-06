import heapq
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:

        pq=[]
        arr=[0]*len(nums)
        for i in nums:
            heapq.heappush(pq,i)
        
        j=0
        while len(pq)!=0:
            alice=heapq.heappop(pq)
            bob=heapq.heappop(pq)

            arr[j]=bob
            j+=1
            arr[j]=alice
            j+=1

            
        return arr




        