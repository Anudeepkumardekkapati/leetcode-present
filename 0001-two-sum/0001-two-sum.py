class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for i in range(len(nums)):
            if nums[i] not in map:

                map[nums[i]]=[i]
            else:
                map[nums[i]].append(i)
        
        for j in range(len(nums)):
            val=target-nums[j]
            if val in map:
                if j!=map[val][-1] :
                    return [j,map[val][-1]]
            
       
        
       



        