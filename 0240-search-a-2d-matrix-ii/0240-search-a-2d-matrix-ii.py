class Solution:
    def searchMatrix(self, nums: List[List[int]], t: int) -> bool:

        sorting = []

        for i in nums:
            sorting += i

        main = sorted(sorting)

        l = 0
        r = len(main) - 1

        while l <= r:

            mid = (l + r) // 2

            if main[mid] == t:
                return True
            elif main[mid] > t:
                r = mid - 1
            else:
                l = mid + 1

        return False