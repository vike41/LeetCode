@ -0,0 +1,29 @@
class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        closest_number = nums[0]
        for num in nums:
            tmp = abs(num)
            if tmp == 0:
                return tmp
            elif tmp <= abs(closest_number):
                closest_number = num
        return closest_number


nums = [-4, -2, 1, 4, 8]
solution = Solution()
solution.findClosestNumber(nums)


class Solution:
    def findClosestNumber(self, nums):
        return min(nums, key=lambda x: (abs(x), -x))

# Test case
nums = [-4, -2, 1, 4, 8]
solution = Solution()
print(solution.findClosestNumber(nums))  # Output: 1