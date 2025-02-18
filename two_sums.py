# https://leetcode.com/problems/two-sum/


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        values = []
        test = sorted(nums)
        for i in range(len(test)):
            for j in range(len(test)):
                if test[i] + test[j] == target:
                    values = [test[i], test[j]]
                elif test[i] + test[j] > target:
                    break
        print(values)
        return nums.index(values[0]), nums.index(values[1])


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    print(solution.twoSum(nums, target))
