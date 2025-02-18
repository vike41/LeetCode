# https://leetcode.com/problems/container-with-most-water/

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        list_length = len(height)
        result = 0
        for i in range(list_length):
            for j in range(i+1, list_length):
                amount = min(height[i], height[j]) * (j - 1)

                result = max(amount, result)
        return result


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    solution = Solution()
    solution.maxArea(height)