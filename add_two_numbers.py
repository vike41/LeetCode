# https://leetcode.com/problems/add-two-numbers/description/

class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        number_1 = ''
        number_2 = ''

        l1.reverse()
        l2.reverse()


        for item in l1:
            number_1 = str(number_1) + str(item)
        #
        for item in l2:
            number_2 = str(number_2) + str(item)

        result = int(number_1) + int(number_2)

        return list(reversed(str(result)))

if __name__ == '__main__':
    l1 = [9, 9, 9, 9, 9, 9, 9]
    l2 = [9, 9, 9, 9]

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    print(result)

